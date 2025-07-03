from backend.app.config import mongodb_connection_url_test, mongodb_database_name_test
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from backend.app.db_schemas import Complaint, ComplaintEntry
import asyncio

async def insert_in_db():
    client = AsyncIOMotorClient(mongodb_connection_url_test)  
    db = client[mongodb_database_name_test] 
    await init_beanie(database=db, document_models=[Complaint])
    