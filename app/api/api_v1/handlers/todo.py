from fastapi import APIRouter, Depends, HTTPException, status
from schemas.todo_schema import TodoDetail, TodoCreate, TodoUpdate
from models.user_model import User
from api.dependencies.user_deps import get_current_user
from services.todo_service import TodoService

todo_router = APIRouter()

@todo_router.get('test')
async def teste():
    return "Notas"

@todo_router.get('/', summary="All notes list", response_model=TodoDetail)
async def list_todo(current_user: User = Depends(get_current_user)):
    notes = await TodoService.list_todos(current_user)
    if notes:
        return await notes
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User has no notes yet")

@todo_router.post('/create', summary="Create a note", response_model=TodoCreate)
async def create_todo(data: TodoCreate, current_user: User = Depends(get_current_user)):
        return await TodoService.create_todo(current_user, data)
    
# @todo_router.get('/detail', summary="note Detail", response_model=TodoDetail)
# async def detail_todo()


@todo_router.put('/update/{todo_id}', summary="Note Update", response_model=TodoUpdate)
async def update_todo(data: TodoUpdate, current_user: User = Depends(get_current_user)):
    pass