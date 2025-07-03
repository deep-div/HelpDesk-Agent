from beanie import Document
from pydantic import BaseModel, Field, EmailStr
from typing import List
from datetime import datetime, timezone
from enum import Enum
import uuid


class ComplaintStatus(str, Enum):
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
    PENDING = "Pending"
    CLOSED = "Closed"


class ComplaintEntry(BaseModel):
    complaint_id: str = Field(default_factory=lambda: str(uuid.uuid4()), unique=True, description="Unique ID for each complaint entry")
    complaint_details: str = Field(..., description="Detailed complaint description")
    status: ComplaintStatus = ComplaintStatus.IN_PROGRESS
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class Complaint(Document):
    name: str = Field(...) # ... means it is compulsory no default value set
    mobile_number: str = Field(..., unique=True, min_length=10, max_length=10, description="Users mobile number")
    email: EmailStr = Field(..., description="Users email", unique=True)
    complaints: List[ComplaintEntry] = Field(..., description="List of complaint entries")
    class Settings:
        name = "complaints"  # mongodb collection name
