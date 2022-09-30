from fastapi import FastAPI
from database import *
from Models import *
from sqlalchemy.orm import Session

app = FastAPI()


@app.post("/")
def create_car_details(car: CarDetails):
    db = Session(engine)
    user = Cars(name=car.name, brand=car.brand)
    db.add(user)
    db.commit()
    return "Item is added"


@app.get("/")
def get_car_details():
    db = Session(engine)
    result = db.query(Cars).all()
    return result
