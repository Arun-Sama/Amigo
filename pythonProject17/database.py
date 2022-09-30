from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

DATABASE_URL = "mysql+pymysql://root:Passwordweak@127.0.0.1:3306/testdb"

db_engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()


class UserInfo(Base):
    __tablename__ = "userinfo"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(250), unique=True)


Base.metadata.create_all(bind=db_engine)
