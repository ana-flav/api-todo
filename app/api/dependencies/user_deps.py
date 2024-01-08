from core.config import settings
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from models.user_model import User
from schemas.auth_schema import TokenPayload
from jose import jwt, JWTError
from services.user_service import UserService
from pydantic import ValidationError
from datetime import datetime
from schemas.auth_schema import TokenPayload

oauth = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login",
    scheme_name="JWT"
)

async def get_current_user(token: str = Depends(oauth)) -> User:
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            settings.ALGORITHM
        )
        token_data = TokenPayload(**payload)
        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException (
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail = "Token expired",
                headers={'WWW-Authenticate':"Bearer"}
            )
    except(JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            details = "Error validation token",
            headers={'WWW-Authenticate':"Bearer"}
        )

    user = await UserService.get_user_by_id(token_data.sub)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found", 
                        headers={'WWW-Authenticate':"Bearer"}
        )
    return user