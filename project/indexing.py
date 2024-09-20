import os
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize HuggingFace embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def index_documents():
    # Load documents from the data folder
    loader = DirectoryLoader('./data', glob="**/*.txt")
    documents = loader.load()

    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)

    # Create and populate Chroma vector store
    vectorstore = Chroma.from_documents(texts, embeddings, persist_directory="./chroma_db")

    print(f"Indexed {len(texts)} document chunks")

    return vectorstore

if __name__ == "__main__":
    vectorstore = index_documents()
    print("Indexing complete. Vector store is ready for querying.")
