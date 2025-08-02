from fastapi import FastAPI
from backend.chat_service.app.apis.chat_routes import chat_router

app = FastAPI()

# Mount the chat-related routes
app.include_router(chat_router)

# py -m uvicorn backend.chat_service.main:app --reload --port 8000
