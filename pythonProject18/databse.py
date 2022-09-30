from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

database_url = "mysql+pymysql://root:Passwordweak@127.0.0.1:3306/college"

engine = create_engine(database_url)
Base = declarative_base()


class User(Base):
    __tablename__ = "Hello"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))


Base.metadata.create_all(bind=engine)
