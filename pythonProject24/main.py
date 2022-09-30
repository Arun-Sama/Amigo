from fastapi import FastAPI, HTTPException, status
from code import TableInfo
from Model import TableDetails

app = FastAPI()

info = TableInfo()


@app.post("/")
def createdetails(table: TableDetails):
    result = info.enterdetails(table)
    if result:
        return result
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The details not found")


@app.get("/")
def getnamedetails():
    result = info.getdetails()
    return result
