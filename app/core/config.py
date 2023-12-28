from typing import List
from decouple import config
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Class for basic config in the project"""
    
    API_V1_STR: str = "/api/v1"
    JWT_REFRESH_SECRET_KEY: str = config("JWT_REFRESH_KEY", cast=str)
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 # seven days
    # BACKEND_CORS_ORIGINS: List[AnyHttpUrl]
    PROJECT_NAME: str = "TODO list"
    
    #Database
    MONGO_CONNECTION_STRING : str = config("MONGO_CONNECTION_STRING", cast=str)
    
    class Config:
        case_sensitive = True 
        
settings = Settings()