from fastapi import FastAPI
from backend.app.clients import insert_in_db
from backend.app.data_models import RegisterComplaint
from backend.app.db_schemas import Complaint
import uvicorn

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await insert_in_db()

@app.post("/register-complaints/")
async def create_complaint(data: RegisterComplaint):
    complaint = Complaint(**data.model_dump())
    await complaint.insert()
    return {"message": "Success", "id": str(complaint.id)}
