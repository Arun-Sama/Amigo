from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine

data_url = "mysql+pymysql://root:Passwordweak@127.0.0.1:3306/college"

engine = create_engine(data_url)

Base = declarative_base()


class Product_details(Base):
    __tablename__ = "Products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    price = Column(Integer)
    summary = Column(String(100))


Base.metadata.create_all(bind=engine)
