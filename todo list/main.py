from fastapi import FastAPI
from model import Todo
from code import Todo_list

app = FastAPI()

todo = Todo_list()


@app.post('/')
def insert_list(dlist: Todo):
    result = todo.insert_list(dlist)
    return result
