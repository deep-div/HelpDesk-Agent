from backend.mongodb_service.app.core.config import mongodb_connection_url_test
from motor.motor_asyncio import AsyncIOMotorClient
from google import genai

#Mongo DB
mongo_db_test_client = AsyncIOMotorClient(mongodb_connection_url_test) 
