from fastapi import FastAPI
from contextlib import asynccontextmanager
from backend.mongodb_service.app.mongodb.db_connections import init_db, close_db
from backend.mongodb_service.app.apis.mongodb_routes  import mongo_router 

@asynccontextmanager
async def lifespan(app: FastAPI): # intialize the db connection once the application is up close it once it is down
    await init_db()
    yield
    await close_db()
    
app = FastAPI(lifespan=lifespan)
    
# Mount the Mongo-related routes
app.include_router(mongo_router)

# py -m uvicorn backend.mongodb_service.main:app --reload --port 8001
