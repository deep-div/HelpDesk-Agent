from pydantic import BaseModel, Field

class ComplaintEntry(BaseModel):
    complaint_details: str = Field(..., description="Detailed complaint description")

class RegisterComplaint(BaseModel):
    name: str = Field(...) 
    mobile_number: str = Field(..., min_length=10, max_length=10, description="Users mobile number")
    complaints: ComplaintEntry= Field(..., description="List of complaint entries")
    
class ComplaintStatus(BaseModel):
    mobile_number: str = Field(..., min_length=10, max_length=10, description="Users mobile number")
    complaint_id: str = Field(..., description="User complaint ID")



