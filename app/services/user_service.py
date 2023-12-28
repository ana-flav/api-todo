from schemas.user_schema import UserAuth
from models.user_model import User

class UserService:
    """Class for user service"""
    
    @staticmethod
    async def create_user(user: UserAuth):
        """Create user"""
        
        user = User(
            username=user.username,
            email=user.email,
            password=user.password
        )
        