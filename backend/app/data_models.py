from pydantic import BaseModel, Field, EmailStr
from typing import List
from enum import Enum

class ComplaintStatus(Enum):
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
    PENDING = "Pending"
    CLOSED = "Closed"


class ComplaintEntry(BaseModel):
    complaint_details: str = Field(..., description="Detailed complaint description")
    status: ComplaintStatus = ComplaintStatus.IN_PROGRESS


class RegisterComplaint(BaseModel):
    name: str = Field(...) 
    mobile_number: str = Field(..., min_length=10, max_length=10, description="Users mobile number")
    email: EmailStr = Field(..., description="Users email")
    complaints: List[ComplaintEntry] = Field(..., description="List of complaint entries")
