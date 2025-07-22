from sqlalchemy.orm import Session
from models import models
from schemas import schemas

def create_author(db:Session, author:schemas.AuthorCreate):
     db_author = models.Author(**author.dict())
     db.add(db_author)
     db.commit()
     db.refresh(db_author)
     return db_author

def get_authors(db:Session, skip: int=0, limit: int=10):
     return db.query(models.Author).offset(skip).limit(limit).all()


def get_author(db:Session, auther_id: int):
     return db.query(models.Author).filter(models.Author.id == auther_id).first()