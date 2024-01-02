from fastapi import APIRouter, HTTPException, status
from schemas.user_schema import UserAuth
from services.user_service import UserService
import pymongo
from pydantic import EmailStr   

user_router = APIRouter()   


from fastapi import HTTPException

@user_router.post("/create", summary="Create User")
async def create_user(data: UserAuth):
    try:
        if not await UserService.is_user(data.email, data.username):
            return await UserService.create_user(data)
      
    except HTTPException as e:
        raise e


        
@user_router.get("/detail/{email}", summary="Detail User")
async def detail_user(email: EmailStr):
    try:
        user = UserService.get_user_by_email(email)
        if user:
            return await user
        raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
