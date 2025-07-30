from fastapi import FastAPI
from contextlib import asynccontextmanager
from backend.app.mongodb.db_connections import insert_in_db, check_user_exists, init_db, close_db, add_complaint_to_user, get_complaint_status
from backend.app.models.data_models import RegisterComplaint, ComplaintStatus
from fastapi import HTTPException

import nest_asyncio
nest_asyncio.apply()

@asynccontextmanager
async def lifespan(app: FastAPI): # intialize the db connection once the application is up close it once it is down
    await init_db()
    yield
    await close_db()
    
app = FastAPI(lifespan=lifespan)
    
@app.post("/register-complaints/")
async def create_complaint(data: RegisterComplaint):
    if not data.mobile_number:
        raise HTTPException(status_code=404, detail= "Missing mobile_number") 
    
    # check if mobile_number is there or not if not there add the complaint and register new user (meaning it is his first complaint)
    obj_id = await check_user_exists(data.mobile_number)
    if not obj_id:
        status = await insert_in_db(data)
        return status
    # user is old and have and already have complaints so will add the new complaint with his old complaints
    return await add_complaint_to_user(mongo_id = obj_id, add_new_complaint = data)
    

@app.post("/status/")
async def check_complaint_status(data: ComplaintStatus):
    if not data.mobile_number:
        raise HTTPException(status_code=404, detail= "Missing mobile_number") 
    
    obj_id = await check_user_exists(data.mobile_number)
    if not obj_id:
        raise HTTPException(status_code=404, detail= "User not Found") 
    
    return await get_complaint_status(obj_id = obj_id, complaint_id = data.complaint_id)
    




# py -m uvicorn backend.app.main:app --reload
