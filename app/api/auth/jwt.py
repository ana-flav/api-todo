from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from services.user_service import UserService
from core.config import settings
from datetime import timedelta
from core.security import create_access_token, create_refresh_token

auth_router = APIRouter()

@auth_router.post('/login')
async def login(data: OAuth2PasswordRequestForm = Depends()) -> Any:
    user = await UserService.authenticate(
        username = data.username, 
        password = data.password
    )
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    data={
        "user_id" : str(user.id),
        "username": user.username
    }
    return {
        "access_token" : create_access_token(data=data, expires_delta=access_token_expires),
        "refresh_token" : create_refresh_token(data=data, expires_delta=access_token_expires)
    }
