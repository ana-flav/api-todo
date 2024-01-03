from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from services.user_service import UserService
from core.config import settings
from datetime import timedelta
from core.security import create_access_token, create_refresh_token
from schemas.auth_schema import TokenSchema
from schemas.user_schema import UserDetail
from api.dependencies.user_deps import get_current_user
from models.user_model import User
from pydantic import ValidationError
from schemas.auth_schema import TokenPayload
from jose import jwt 
from uuid import UUID, uuid4

auth_router = APIRouter()

@auth_router.post('/login', summary="Create Access Token and Refresh Token", response_model=TokenSchema)
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

    return {
        "access_token" : create_access_token(user.user_id, expires_delta=access_token_expires),
        "refresh_token" : create_refresh_token(user.user_id, expires_delta=access_token_expires)
    }

@auth_router.post('/test-token', summary='Test Token', response_model=UserDetail)
async def test_token(user: User = Depends(get_current_user)):
    return user

@auth_router.post("/refresh-token", summary="Refresh Token", response_model = TokenSchema)
async def refresh_token(refresh_token: str = Body(...)):
    try:
        paylaod = jwt.decode(
            refresh_token,
            settings.JWT_REFRESH_SECRET_KEY,
            settings.ALGORITHM
        )
        token_data = TokenPayload(**paylaod)

    except:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Validation Error', 
            headers={'WWW-Authenticate': 'Bearer'}
        )
    user = await UserService.get_user_by_id(token_data.sub)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail='User not found', 
            headers={'WWW-Authenticate': 'Bearer'}
        )

    return {
        'access_token': create_access_token(user.user_id),
        'refresh_token': create_refresh_token(user.user_id)
    }