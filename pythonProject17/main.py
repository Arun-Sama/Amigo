from fastapi import FastAPI, Depends
from pydantic import BaseModel
from database import SessionLocal, UserInfo
from sqlalchemy.orm import Session

app = FastAPI()


class UserDetails(BaseModel):
    username: str = ""
    id: int

    class Config:
        orm_mode = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/")
def printHello(user: UserDetails, db: Session = Depends(get_db)):
    u = UserInfo(name=user.username, id=user.id)
    db.add(u)
    db.commit()
    return u
