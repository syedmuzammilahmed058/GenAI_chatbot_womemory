
# GenAI Chatbot using FastAPI and Ollama

## Project Overview

A simple Generative AI chatbot developed using FastAPI, LangChain and Ollama.

The application uses the Llama 3.1 (8B) Large Language Model to generate responses based on user input.

This is a stateless chatbot. Each request is processed independently without retaining previous conversation history.

## Technology Stack

- Python
- FastAPI
- LangChain
- Ollama
- Llama 3.1 (8B)
- Pydantic

## Architecture

User Input
    |
    v
FastAPI API Endpoint
    |
    v
ChatRequest Validation
    |
    v
LangChain
    |
    v
Ollama - Llama 3.1 (8B)
    |
    v
Generated Response
    |
    v
API Response to User

## Project Structure

GenAI_Chatbot_Without_Memory/
|
|-- main.py
|-- requirements.txt
|-- README.md
|-- .gitignore

## Prerequisites

- Python 3.10+
- Ollama installed
- Llama 3.1 (8B) model

## Installation

Install dependencies:

pip install -r requirements.txt

Download the model:

ollama pull llama3.1:8b

## Run Application

uvicorn main:app --reload

Application URL:

http://127.0.0.1:8000

Swagger Documentation:

http://127.0.0.1:8000/docs

## API Endpoint

POST /chat

Request:

{
    "message": "Explain Generative AI"
}

Response:

{
    "response": "Generative AI is..."
}

## Key Features

- REST API using FastAPI
- LLM integration using LangChain
- Local model execution using Ollama
- Request validation using Pydantic
- Stateless request processing

## Future Enhancements

- Conversational memory
- Chat history management
- Streaming responses
- Frontend integration

## Author

Syed Muzammil Ahmed
GenAI Engineer | Python | LLMs | RAG | Agentic AI 
