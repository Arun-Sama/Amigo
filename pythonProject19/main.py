from fastapi import FastAPI
from sqlalchemy.orm import Session
from database import Details, engine
# from Model import UserDetails
from Code import Name

app = FastAPI()

info = Name()


@app.get("/")
def get_result():
    db = Session(engine)
    myresult = db.query(Details).all()
    return myresult


@app.post("/")
def printhello(user_name: str, number: int):
    result = info.hello(user_name, number)
    return {"Hello": result}
