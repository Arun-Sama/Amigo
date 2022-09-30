from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer,DateTime
from sqlalchemy.ext.declarative import declarative_base

dataurl = "mysql+pymysql://root:Passwordweak@127.0.0.1:3306/testdb"

engine = create_engine(dataurl)

Base = declarative_base()


class Todolist(Base):
    __tablename__ = "Todo List"
    id = Column(Integer, primary_key=True, autoincrement=True)
    task = Column(String)
    sub_task = Column(String)
    date = Column(DateTime)
    list = Column(String)

