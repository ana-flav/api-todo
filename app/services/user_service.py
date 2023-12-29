from schemas.user_schema import UserAuth
from models.user_model import User
from core.security import get_password, verify_password
from typing import Optional


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
    async def get_user_by_email(username: str) -> Optional[User]:
        return await User.find_one(User.username==username)
    
    @staticmethod 
    async def authenticate(username: str, password: str) -> Optional[User]:

        try:
            user = await UserService.get_user_by_email(username)
            if not user:
                return None
            if not verify_password(password=password, hashed_password=user.password):
                return False
            return user 
        except Exception as e:
            print(e)
        
        