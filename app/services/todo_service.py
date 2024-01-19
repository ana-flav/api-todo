from models.user_model import User 
from models.todo_model import Todo
from typing import List
from schemas.todo_schema import TodoCreate, TodoUpdate


class TodoService:
    @staticmethod
    async def list_todos(user: User) -> List[Todo]:
        todos = await Todo.find(Todo.owner.id == user.user_id).to_list()
        return todos
    
    @staticmethod
    async def create_todo(user: User, data: TodoCreate) -> Todo:
        # breakpoint()
        data = data.model_dump()
        data.update({"owner": user})
        todo = Todo(
                title=data['title'],
                description=data['description'],
                owner=data['owner'],
                status=data['status'],
                )
        breakpoint()
        return await todo.insert()
    
    # @staticmethod
    # async def update_todo(user: User, data: TodoUpdate):
        
    
    