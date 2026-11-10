from fastapi import FastAPI
from pydantic import BaseModel
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

# Initialize FastAPI
app = FastAPI()

# Initialize LLM
llm = ChatOllama(
    model="llama3.1:8b",
    temperature=0.7
)

# Request schema
class ChatRequest(BaseModel):
    message: str

# Response schema
class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    # Send only current message (no memory)
    response = llm.invoke([
        HumanMessage(content=req.message)
    ])

    return {
        "response": response.content
    }
@app.get("/")
def home():
    return {"message": "Welcome to GenAI Chatbot"}