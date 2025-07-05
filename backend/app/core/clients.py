from backend.app.core.config import mongodb_connection_url_test, gemini_flash_test
from motor.motor_asyncio import AsyncIOMotorClient
from google import genai

#Mongo DB
mongo_db_test_client = AsyncIOMotorClient(mongodb_connection_url_test) 

#Gemini
gemini_client_test = genai.Client(api_key=gemini_flash_test)
