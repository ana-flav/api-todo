from pydantic import BaseModel, EmailStr, Field

class UserAuth():
    """Class for user authentication"""
    
    email: EmailStr = Field(..., description="User email") 
    username: str = Field(..., description="Username") 
    password: str = Field(..., description="User password")

    
