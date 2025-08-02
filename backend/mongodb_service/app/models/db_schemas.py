from beanie import Document
from pydantic import BaseModel, Field
from typing import Dict
from datetime import datetime
from zoneinfo import ZoneInfo  
from enum import Enum


class ComplaintStatus(str, Enum):
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
    PENDING = "Pending"
    CLOSED = "Closed"


class ComplaintDetails(BaseModel):
    complaint_details: str = Field(..., description="Detailed complaint description")
    status: ComplaintStatus = ComplaintStatus.IN_PROGRESS
    created_at: datetime = Field(default_factory=lambda: datetime.now(ZoneInfo("Asia/Kolkata")))


class Complaint(Document):
    name: str = Field(...)
    mobile_number: str = Field(..., min_length=10, max_length=10)
    complaints: Dict[str, ComplaintDetails] = Field(..., description="Complaint ID mapped to complaint details")
    class Settings:
        name = "complaints"
