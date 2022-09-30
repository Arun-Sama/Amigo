from sqlalchemy.testing import db

from Model import TableDetails
from database import Table, engine
from sqlalchemy.orm import Session


class TableInfo:

    def enterdetails(self, table: TableDetails):
        try:
            db = Session(engine)
            nameInfo = Table(name=table.name)
            db.add(nameInfo)
            db.commit()
            return table
        except Exception as error:
            print("Unexpected error:", error)

    def getdetails(self):
        db = Session(engine)
        result = db.query(Table).all()
        myresult = []
        for value in result:
            myresult.append(value.name)
        return {"Result": myresult}
