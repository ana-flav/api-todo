
from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Indexed, Link, before_event, Replace, Insert
from pydantic import Field
from .user_model import User

class Todo(Document):
    """Todo model"""
    
    todo_id: UUID = Field(UUID)
    status: bool = False
    title: Indexed(str)
    description: Indexed(str)
    created_at: datetime = Field(default=datetime.now)
    updated_at: datetime = Field(default=datetime.now)
    owner: Link[User]

    def __repr__(self) -> str:
        return f"<Todo f{self.title}>"
    
    def __str__(self) -> str:
        return self.title
    
    def __hash__(self) -> int:
        return hash(self.title)
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Todo):
            return self.todo_id == other.todo_id
        return False

    # whenever there is an insert or update occurs, 
    # the functions are called and the field updated_at is modified
    @before_event([Replace, Insert])
    def sync_update_at(self):
        self.updated_at = datetime.utcnow()
    