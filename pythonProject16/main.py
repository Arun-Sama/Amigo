from typing import List
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Todo(BaseModel):
    num: int
    name: str
    description: str


app = FastAPI(title="todo API")

store_todo = []


@app.get('/')
def home():
    return "Hello"


@app.post('/todo/')
def create_todo(todo: Todo):
    store_todo.append(todo)
    return todo


@app.get('/todo/')
def get_all_todo():
    return store_todo


@app.get('/todo{id}')
def get_todo(id: int):
    try:
        return store_todo[id]

    except:
        raise HTTPException(status_code=404, detail="Todo Not Found")


@app.put('/todo/{id}')
def update_todo(id: int, todo: Todo):
    try:
        store_todo[id] = todo
        return store_todo[id]


    except:
        raise HTTPException(status_code=404, detail="Todo Not Found")


@app.delete('/todo/{id}')
def delete_todo(id: int):
    try:
        obj = store_todo[id]
        store_todo.pop(id)
        return obj

    except:
        raise HTTPException(status_code=404, detail="Todo Not Found")


uvicorn.run(app)