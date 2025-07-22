from sqlalchemy.orm import Session
from models import models
from schemas.schemas import BookCreate, BookUpdate 

# Create a new book with a given author_id
def create_book(db: Session, book: BookCreate, author_id: int):
    db_book = models.Book(**book.dict(), author_id=author_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Get a paginated list of all books
def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Book).offset(skip).limit(limit).all()

# Get a single book by its ID
def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

# Get all books written by a specific author
def get_books_by_author_id(db: Session, author_id: int):
    return db.query(models.Book).filter(models.Book.author_id == author_id).all()



def update_book(db: Session, book_id: int, book_update: BookUpdate):  # <- Use BookUpdate here
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book is None:
        return None
    
    if book_update.title is not None:
        db_book.title = book_update.title
    if book_update.description is not None:
        db_book.description = book_update.description
    if book_update.author_id is not None:
        db_book.author_id = book_update.author_id

    db.commit()
    db.refresh(db_book)
    return db_book