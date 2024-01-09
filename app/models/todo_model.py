from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Indexed, Link, before_event, Replace, Insert
from pydantic import Field
from .user_model import User

class Todo(Document):
    """Todo model"""
    
    todo_id = UUID = Field(default_factory=uuid4, unique=True)
    status: bool = False
    title: Indexed(str)
    description: Indexed(str)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    owner: Link[User]