from pydantic import BaseModel, EmailStr, Field

from uuid import UUID
from typing import Optional

class UserAuth(BaseModel):
    """Class for user authentication"""
    
    email: EmailStr = Field(...,description="User email") 
    username: str = Field(..., min_length=5, max_length=50, description="Username") 
    password: str = Field(..., min_length=5, max_length=50,  description="User password")
 
class UserDetail(BaseModel):
    """Class for user details"""
    
    user_id: UUID
    username: str
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
    is_active: Optional[bool]
    