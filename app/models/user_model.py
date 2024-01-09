from beanie import Document, Indexed
from uuid import UUID, uuid4
from pydantic import Field, EmailStr
from datetime import datetime, date
from typing import Optional

class User(Document):
    """User model"""
    
    user_id: UUID = Field(uuid4, default_factory=uuid4)
    username: Indexed(str, unique=True)    
    email: Indexed (EmailStr, unique=True)
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.now)  
     
    def __str__(self) -> str:
        return self.email

    def __repr__(self) -> str:
        return f"<User {self.email} - {self.username}>"
    
    def __hash__(self) -> int:
        return hash(self.email)
    
    def __eq__(self, object: object) -> bool:
        if isinstance(object, User):
            return self.email == object.email
        return False
    