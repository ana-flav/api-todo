from fastapi import HTTPException, status
from schemas.user_schema import UserAuth
from models.user_model import User
from core.security import get_password, verify_password
from typing import Optional
from pydantic import EmailStr

class UserService:
    """Class for user service"""
    
    @staticmethod
    async def create_user(user: UserAuth):
        """Create user"""
        
        user = User(
            username=user.username,
            email=user.email,
            password=get_password(user.password)
        )
    
        await user.save()
        return user
    
    @staticmethod
    async def get_user_by_username(username: str) -> Optional[User]:
        return await User.find_one(User.username==username)
    
    @staticmethod 
    async def authenticate(username: str, password: str) -> Optional[User]:

        try:
            user = await UserService.get_user_by_username(username)
            if not user:
                return None
            if not verify_password(password=password, hashed_password=user.password):
                return False
            return user 
        except Exception as e:
            print(e)
    
    @staticmethod
    async def get_user_by_email(email: EmailStr) -> Optional[User]:
        return await User.find_one(User.email==email)

    @staticmethod
    async def is_user(email: EmailStr, username: str) -> None:

        if await UserService.get_user_by_email(email) or await UserService.get_user_by_username(username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username or Email already exists."
            )
        