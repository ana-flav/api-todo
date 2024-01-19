from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime


class TodoCreate(BaseModel):
    """Todo Create"""

    title: str = Field(..., title='Title', min_length=5, max_length=35)
    description: str = Field(..., title='Description', min_length=5, max_length=150)
    status: Optional[bool] = False
    
    
class TodoUpdate(BaseModel):
    """Todo Update"""
    
    title: Optional[str] 
    description: Optional[str] 
    status: Optional[bool] = False
    

class TodoDetail(BaseModel):
    """Todo Detail"""
    
    todo_id: UUID
    status: bool
    title: str
    description: str
    created_at: datetime
    updated_at: datetime