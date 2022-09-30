from database import engine, Details
from sqlalchemy.orm import Session
from Model import UserDetails


class Name:

    def hello(self, user_name, number):
        db = Session(engine)
        user = UserDetails(name=user_name, num=number)
        # user.name = name
        # user.num = num
        update = Details(name=user.name)
        db.add(update)
        db.commit()
        return user_name









