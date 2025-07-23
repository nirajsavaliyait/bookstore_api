import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



DATABASE_URL = "postgresql://bookstore_db_qsqc_user:M84vZoIuBG5qbucMTMejRzpb3DiQ17rp@dpg-d1vlbgndiees73bpct0g-a.oregon-postgres.render.com/bookstore_db_qsqc"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit= False, autoflush= False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

