from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

# from sqlalchemy.orm import sessionmaker


url = "mysql+pymysql://root:Passwordweak@127.0.0.1:3306/testdb"

engine = create_engine(url)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Names(Base):
    __tablename__ = "Name"
    name = Column(String(200), primary_key=True)


Base.metadata.create_all(bind=engine)
