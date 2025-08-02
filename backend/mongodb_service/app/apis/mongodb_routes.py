from fastapi import APIRouter, HTTPException
from backend.mongodb_service.app.models.data_models import RegisterComplaint, ComplaintStatus
from backend.mongodb_service.app.mongodb.db_connections import (
    insert_in_db,
    check_user_exists,
    add_complaint_to_user,
    get_complaint_status,
)

mongo_router = APIRouter()

@mongo_router.post("/register-complaint-mongodb/")
async def create_complaint(data: RegisterComplaint):
    if not data.mobile_number:
        raise HTTPException(status_code=404, detail="Missing mobile_number")
    
    obj_id = await check_user_exists(data.mobile_number)
    if not obj_id:
        return await insert_in_db(data)
    return await add_complaint_to_user(mongo_id=obj_id, add_new_complaint=data)

@mongo_router.post("/check-complaint-status-mongodb/")
async def check_complaint_status(data: ComplaintStatus):
    if not data.mobile_number:
        raise HTTPException(status_code=404, detail="Missing mobile_number")
    
    obj_id = await check_user_exists(data.mobile_number)
    if not obj_id:
        raise HTTPException(status_code=404, detail="User not Found")
    
    return await get_complaint_status(obj_id=obj_id, complaint_id=data.complaint_id)
