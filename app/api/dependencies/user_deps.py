from fastapi.security import OAuth2PasswordBearer
from core.config import settings
from fastapi import Depends
from models.user_model import User
from jose import JWTError

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login"
    scheme_name="JWT"
)