from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USER='root'
PASSWORD='Sql%401236'
HOST='localhost'
DATABASE='fastapi_db'
PORT=3306

DATABASE_URL=f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

#CONNECTION
engine=create_engine(DATABASE_URL)

SessionLocal=sessionmaker(autoflush= False, autocommit=False, bind=engine)

#Base
Base=declarative_base()