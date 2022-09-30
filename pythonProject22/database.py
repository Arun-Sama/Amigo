from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

db_url = "mysql+pymysql://root:Passwordweak@127.0.0.1:3306/college"

engine = create_engine(db_url)

Base = declarative_base()


class Cars(Base):
    __tablename__ = "Brand"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    brand = Column(String(200))

Base.metadata.create_all(engine)
