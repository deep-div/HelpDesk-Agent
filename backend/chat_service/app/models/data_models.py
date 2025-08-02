from pydantic import BaseModel, Field
from typing import List

class Message(BaseModel):
    role: str = Field(..., description="Role of the sender: 'user' or 'assistant'")
    content: str = Field(..., description="Content of the message")

class Prompt(BaseModel):
    session_id: str = Field(..., description="Unique session identifier for the user")
    user_query: str = Field(..., description="User Prompt")
    history: List[Message] = Field(..., description="List of previous chat messages")

