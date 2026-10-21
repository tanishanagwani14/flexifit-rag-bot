import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rag_engine import ask_flexifit_bot

app = FastAPI(
    title="FlexiFit AI Chatbot API",
    description="Backend API powering the RAG chatbot for FlexiFit Physiotherapy Clinic",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.get("/")
def read_root():
    return {"status": "online", "message": "FlexiFit RAG API is running cleanly."}

@app.post("/api/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    user_message = request.message.strip()
    
    if not user_message:
        raise HTTPException(status_code=400, detail="Message cannot be empty.")
    
    try:
        bot_reply = ask_flexifit_bot(user_message)
        return ChatResponse(response=bot_reply)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating response: {str(e)}")