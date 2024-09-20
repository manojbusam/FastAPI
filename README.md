# FastAPI Project using LLM

This project demonstrates a FastAPI application designed to provide detailed information about the NextGen Smartwatch. It includes a backend API for querying smartwatch features and a React frontend for interacting with the API.

## Features

- **FastAPI Backend**: 
  - Provides an endpoint to query smartwatch features.
  - Uses ChromaDB for efficient document storage and retrieval.
  - Supports embedding generation using SentenceTransformer.

- **React Frontend**: 
  - Mimics a chat interface for querying the API.
  - Displays results in a user-friendly format.

## Getting Started

### Backend Setup

1. **Install Dependencies**:
   Ensure you have Python installed, then run:
   ```bash
   pip install fastapi uvicorn chromadb langchain
   ```

2. **Run the Backend Server**:
   Execute the following command to start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

3. **Test the API**:
   Use the following `curl` command to query the API:
   ```bash
   curl -X POST "http://localhost:8000/query" \
        -H "Content-Type: application/json" \
        -d '{"text": "What are the key features of the NextGen Smartwatch?", "n_results": 3}'
   ```

### Frontend Setup

1. **Navigate to Frontend Directory**:
   Ensure you are in the frontend directory where your React app is located.

2. **Install Node.js Dependencies**:
   Run this command to install necessary packages:
   ```bash
   npm install
   ```

3. **Start the React App**:
   Launch your React frontend with:
   ```bash
   npm start
   ```

4. **Access the UI**:
   Open your browser and navigate to `http://localhost:3000` to interact with the application.

## Scripts

- **Backend Setup Script**: `be-setup.sh`
  - Automates backend setup and indexing of documents.
  
- **Frontend Setup Script**: `fe-setup.sh`
  - Automates frontend setup and starts the React development server.

## Example Output

When querying for features of the NextGen Smartwatch, expect detailed, structured responses including sections like:

- Getting Started
- Basic Operations
- Health and Fitness Features
- Smart Assistant
- Troubleshooting

Each section provides concise bullet points for easy understanding.



<img width="847" alt="Screenshot 2024-09-19 at 8 23 17 PM" src="https://github.com/user-attachments/assets/2772868c-e20c-4ff8-a369-9d6454ec53d3">
