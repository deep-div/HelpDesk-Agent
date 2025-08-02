from backend.chat_service.app.core.config import gemini_flash_test
from google import genai


#Gemini
gemini_client_test = genai.Client(api_key=gemini_flash_test)
