from sqlalchemy.orm import Session

# import Models
from model import *
from database import engine, Names


class NameInfo:

    def enterdetails(self, user_name):
        try:
            db = Session(engine)
            user = NameDetails(name=user_name)
            name_info = Names(name=user.name)
            db.add(name_info)
            db.commit()
            return name_info
        except Exception as error:
                print("Unexpected error:", error)

    def get_details(self):
        db = Session(engine)
        result = db.query(Names.name).all()
        return result

    def get_details_name(self, name):
        db = Session(engine)
        result = db.query(Names).filter(Names.name == name).first()
        return result

    def update_details(self, user_name, user_name2):
        db = Session(engine)
        result = db.query(Names).filter(Names.name == user_name).update({'name': user_name2})
        db.commit()
        return "The details is updated"

    def delete_details(self, user_name):
        db = Session(engine)
        result = db.query(Names).filter(Names.name == user_name).delete()
        db.commit()
        return "It is deleted"
