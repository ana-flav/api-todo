from fastapi import APIRouter, HTTPException, status
from schemas.user_schema import UserAuth
from services.user_service import UserService
import pymongo
from pydantic import EmailStr   

user_router = APIRouter()   


@user_router.post("/create", summary="Create User")
async def create_user(data:UserAuth):
    try:
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or Email already exists."
        )
        
@user_router.get("/detail/{email}", summary="Detail User")
async def detail_user(email: EmailStr):
    try:
        user = UserService.get_user_by_email(email)
        if user:
            return await user
        raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
