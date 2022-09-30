from typing import Optional
from fastapi import FastAPI
from todo.model.model import Todo, Todo_pydantic, TodoIn_pydantic
from pydantic import BaseModel
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

app = FastAPI()


@app.get("/")
async def get_words():
    return {"Hello": "World"}


class status(BaseModel):
    message: str


@app.post("/todos", response_model=Todo_pydantic)
async def create_todo(todo: TodoIn_pydantic):
    todo_obj = await Todo.create(**todo.dict(exclude_unset=True))
    return await Todo_pydantic.from_tortoise_orm(todo_obj)


register_tortoise(
    app,
    db_url="mysql+pymysql://root:Passwordweak@127.0.0.1:3306/testdb",
    modules={"models": ["todo.model.model"]},
    generate_schemas=True,
    add_exception_handlers=True

)
