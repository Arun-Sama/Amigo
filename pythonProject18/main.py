from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session

from databse import User, engine

app = FastAPI()


class UserDetails(BaseModel):
    name = ""

    class Config:
        orm_mode = True


@app.post("/")
def printHello(user: UserDetails):
    db = Session(engine)
    u = User(name=user.name)
    db.add(u)
    db.commit()
    return {"Hello": user.name}
