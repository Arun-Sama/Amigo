from fastapi import FastAPI, HTTPException, status

# import database
from model import NameDetails
from code import NameInfo
from typing import *

# from database import *
# from sqlalchemy.orm import Session

app = FastAPI()

info = NameInfo()


@app.post("/")
def create_name_details(user_name: str):
    result = info.enterdetails(user_name)
    if result:
        return result

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The id already created")


@app.get("/")
def get_name_details():
    myresult = info.get_details()
    return myresult


@app.get("/{name}")
def get_name_details(name: str):
    myresult = info.get_details_name(name)
    if myresult:
        return myresult

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The details not found")


@app.put("/{name}")
def update_car_details(user_name: str, user_name2: str):
    myresult = info.update_details(user_name, user_name2)
    if myresult:
        return myresult

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The details not found")


@app.delete("/{name}")
def delete_car_details(user_name: str):
    myresult = info.delete_details(user_name)
    if myresult:
        return myresult

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The details not found")
