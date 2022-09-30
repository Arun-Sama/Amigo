import datetime
from pydantic import BaseModel
from typing import Optional


class Todo(BaseModel):
    Id = int
    Task = str
    Sub_task = str
    Date = datetime.date
    List = str

    class Config:
        orm_mode = True
