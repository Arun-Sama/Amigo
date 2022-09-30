from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker

db_url = "mysql+pymysql://root:Passwordweak@127.0.0.1:3306/testdb"

engine = create_engine(db_url)
Base = declarative_base()


class Details(Base):
    __tablename__ = "Todo"
    num = Column(Integer, primary_key=True,index=True)
    name = Column(String(250))


Base.metadata.create_all(bind=engine)
