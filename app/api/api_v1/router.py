from fastapi import APIRouter   
from api.api_v1.handlers import user
from api.auth.jwt import auth_router

router = APIRouter()

router.include_router(
    user.user_router,
    prefix="/users",
    tags=["users"]  
)    

router.include_router(
    auth_router,
    prefix='/auth',
    tags=['auth']
)