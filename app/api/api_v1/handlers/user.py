from fastapi import APIRouter, HTTPException, status, Depends
from schemas.user_schema import UserAuth, UserDetail
from services.user_service import UserService
import pymongo
from pydantic import EmailStr  
from models.user_model import User
from api.dependencies.user_deps import get_current_user

user_router = APIRouter()   


from fastapi import HTTPException

@user_router.post("/create", summary="Create User", response_model=UserDetail)
async def create_user(data: UserAuth):
    try:
        if not await UserService.is_user(data.email, data.username):
            return await UserService.create_user(data)
      
    except HTTPException as e:
        raise e


@user_router.get("/detail/{email}", summary="Detail User", response_model=UserDetail)
async def detail_user(email: EmailStr):
    try:
        user = UserService.get_user_by_email(email)
        if user:
            return await user
        raise HTTPException(status_code=404, detail="User not found" )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
@user_router.get("/current_user", summary="Current User", response_model=UserDetail)
async def detail_current_user(user: User = Depends(get_current_user)):
    return user