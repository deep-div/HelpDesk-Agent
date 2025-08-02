from fastapi import APIRouter
from backend.chat_service.app.gemini.gemini_tools import GeminiTools
from backend.chat_service.app.models.data_models import Prompt
from backend.chat_service.app.gemini.gemini_llm import GeminiLLM

chat_router = APIRouter()

geminillm = GeminiLLM()
geminitools = GeminiTools(geminillm)

@chat_router.post("/chat-get-prompt-from-ui")
async def chat_with_agent(data: Prompt):
    history = data.history
    prompt = data.user_query
    
    agent_response = geminitools.pick_right_tool(prompt, history)

    return {"agent_response": agent_response}
