import pandas as pd
from sqlalchemy import Column,Integer,String,Numeric
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

engine=create_engine("mysql+mysqlconnector://root:password@localhost:3306/gg")

Base=declarative_base()

class Gtable(Base):
    __tablename__="gtable"
    __table_args__={"schema":"gg"}

    id=Column(Integer,primary_key=True)
    name=Column(String(250),nullable=True)
    platform=Column(String(250),nullable=True)
    release_date=Column(String(250),nullable=True)
    summary=Column(String(500),nullable=True)
    review=Column(Numeric(25),nullable=True)

Base.metadata.create_all(engine)

file="video_games.csv"

df=pd.read_csv(file)

df.to_sql(con=engine,name=Gtable.__tablename__,if_exists="append",index=False)

session=sessionmaker()
session.configure(bind=engine)
s=session()

