import os
import logging
from typing import List, Dict
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import chromadb
from chromadb.utils import embedding_functions
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow React app origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize ChromaDB client
chroma_client = chromadb.Client()

# Initialize embedding function
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# Initialize text splitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

def load_and_chunk_documents(directory: str) -> List[Dict]:
    chunked_docs = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            loader = TextLoader(file_path)
            document = loader.load()[0]
            chunks = text_splitter.split_text(document.page_content)
            for i, chunk in enumerate(chunks):
                chunked_docs.append({
                    "text": chunk,
                    "metadata": {
                        "source": filename,
                        "chunk": i,
                        **document.metadata
                    }
                })
    return chunked_docs

def index_documents(documents: List[Dict]):
    collection = chroma_client.create_collection(name="smartwatch_docs", embedding_function=embedding_function)
    
    for doc in documents:
        collection.add(
            documents=[doc["text"]],
            metadatas=[doc["metadata"]],
            ids=[f"{doc['metadata']['source']}_{doc['metadata']['chunk']}"]
        )
        logger.info(f"Indexed document: {doc['metadata']['source']}, chunk {doc['metadata']['chunk']}")

    logger.info(f"Indexing complete. Total documents indexed: {len(documents)}")

# Output parser function for better formatting
def parse_output(text):
    lines = text.split('\n')
    parsed_text = []
    
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith(('1.', '2.', '3.', '4.', '5.')):
            parsed_text.append(f"\nRegarding {stripped_line[2:].strip()}:")  # Remove number and period
        elif stripped_line.startswith('-'):
            bullet_point = stripped_line[1:].strip()
            parsed_text.append(f"• {bullet_point.capitalize()}")
        elif stripped_line:
            parsed_text.append(stripped_line)
    
    response = "Here's what I found about the NextGen Smartwatch:\n\n" + "\n".join(parsed_text)
    return response

# Index documents on startup
documents = load_and_chunk_documents("./project/data")
index_documents(documents)

class Query(BaseModel):
    text: str
    n_results: int = 5

@app.post("/query")
async def query_documents(query: Query):
    collection = chroma_client.get_collection("smartwatch_docs")
    results = collection.query(
        query_texts=[query.text],
        n_results=query.n_results
    )
    
    if not results['documents'][0]:
        raise HTTPException(status_code=404, detail="No matching documents found")
    
    return {
        "query": query.text,
        "results": [
            {
                "text": parse_output(doc),  # Ensure this function formats without extra prefixes
                "metadata": meta,
                "distance": dist
            }
            for doc, meta, dist in zip(results['documents'][0], results['metadatas'][0], results['distances'][0])
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)