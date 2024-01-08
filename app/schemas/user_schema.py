from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from typing import Optional
from datetime import date 

class UserAuth(BaseModel):
    """Class for user authentication"""
    
    email: EmailStr = Field(...,description="User email") 
    username: str = Field(..., min_length=5, max_length=50, description="Username") 
    password: str = Field(..., min_length=5, max_length=50,  description="User password")
    first_name: Optional[str] = Field(None, min_length=5, max_length=50, description="First name")
    last_name: Optional[str] = Field(None, min_length=5, max_length=50, description="Last name")
    date_of_birthday: Optional[date] = Field(None, description= "Date of Birthday")
    
    
class UserDetail(BaseModel):
    user_id: UUID
    username: str
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
    disabled: Optional[bool]
    date_of_birthday: Optional[date]
