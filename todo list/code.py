from model import Todo
from database import *
from sqlalchemy.orm import Session


class Todo_list:

    def insert_list(self, dolist: Todo):
        db = Session(engine)
        details = Todolist(tolist=dolist.List)
        db.add(details)
        db.commit()
        return dolist
