from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
# from typing import List

url = "mysql+pymysql://root:Passwordweak@127.0.0.1:3306/college"

engine = create_engine(url)

Base = declarative_base()


class Table(Base):
    __tablename__ = "Name"
    name = Column(String(250), primary_key=True)


Base.metadata.create_all(bind=engine)
