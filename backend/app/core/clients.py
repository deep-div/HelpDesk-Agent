from backend.app.core.config import mongodb_connection_url_test
from motor.motor_asyncio import AsyncIOMotorClient

mongo_db_test_client = AsyncIOMotorClient(mongodb_connection_url_test)  


    