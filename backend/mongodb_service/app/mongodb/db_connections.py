from backend.mongodb_service.app.core.config import mongodb_database_name_test
from backend.mongodb_service.app.core.clients import mongo_db_test_client
from beanie import init_beanie
from backend.mongodb_service.app.models.db_schemas import Complaint, ComplaintDetails
from backend.mongodb_service.app.models.data_models import RegisterComplaint
from bson import ObjectId
from fastapi import HTTPException
import uuid
client = mongo_db_test_client  

async def init_db():
    db = client[mongodb_database_name_test]
    await init_beanie(database=db, document_models=[Complaint])

async def close_db():
    client.close()

async def insert_in_db(data: RegisterComplaint):
    complaint_id = str(uuid.uuid4())
    complaint_detail = ComplaintDetails(
        complaint_details=data.complaints.complaint_details,
    )
    complaint = Complaint(
        name=data.name,
        mobile_number=data.mobile_number,
        complaints={complaint_id: complaint_detail}
    )
    await complaint.insert()
    return {"message": "Success", "Complaint id": complaint_id}


async def check_user_exists(mobile_number: str):
    if not mobile_number :
        raise HTTPException(status_code=404, detail="Missing mobile number")
    user = await Complaint.find_one({"mobile_number": mobile_number})
    
    return str(user.id) if user else False


async def add_complaint_to_user(mongo_id: str, add_new_complaint: RegisterComplaint):
    obj_id = ObjectId(mongo_id)
    complaint_doc = await Complaint.get(obj_id)

    if not complaint_doc:
        raise HTTPException(status_code=404, detail="Complaint document with given ID not found")

    complaint_id = str(uuid.uuid4())

    complaint_detail = ComplaintDetails(
        complaint_details=add_new_complaint.complaints.complaint_details,
    )
    complaint_doc.complaints[complaint_id] = complaint_detail
    await complaint_doc.save()
    return {"message": "New complaint added", "complaint_id": complaint_id}


async def get_complaint_status(obj_id: str, complaint_id: str):
    mongo_obj_id = ObjectId(obj_id)
    user  = await Complaint.get(mongo_obj_id)
    complaint = user.complaints.get(complaint_id) # find user complaint from object id
    
    if not complaint:
        raise HTTPException(status_code=404, detail="Complaint not found for this user")

    return {
        "complaint_id": complaint_id,
        "status": complaint.status,
        "details": complaint.complaint_details,
        "created_at": complaint.created_at
    }

