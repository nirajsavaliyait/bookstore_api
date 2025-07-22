from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import schemas
from models import models 
from src import author, book
from database.database import get_db


router = APIRouter()


@router.post("/authors/", response_model=schemas.Author)
def create_author_route(author_data: schemas.AuthorCreate, db: Session = Depends(get_db)):
    try:
        return author.create_author(db=db, author=author_data)  
    except Exception as e:
        print("❌ ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/authors/", response_model=list[schemas.Author])  
def get_authors_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return author.get_authors(db, skip=skip, limit=limit)



@router.get("/authors/{author_id}", response_model=schemas.Author)
def get_author_by_id(author_id: int, db: Session = Depends(get_db)):
    db_author = author.get_author(db, author_id)  
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author

@router.post("/books/", response_model=schemas.Book)
def create_book_route(book_data: schemas.BookCreate, author_id: int, db: Session = Depends(get_db)):
    return book.create_book(db, book_data, author_id)



@router.get("/books/", response_model=list[schemas.Book])
def get_books_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):  
        return book.get_books(db, skip=skip, limit=limit)


@router.get("/books/{book_id}", response_model=schemas.Book)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):  
        db_book = book.get_book(db, book_id)
        if not db_book:
            raise HTTPException(status_code=404, detail="Book not found")
        return db_book

@router.get("/books/by-author/{author_id}", response_model=list[schemas.Book])
def get_books_by_author(author_id: int, db: Session = Depends(get_db)):
    db_book =  book.get_books_by_author_id(db, author_id)
    if not db_book :
        raise HTTPException(status_code=404, detail="Author_id not found")
    return db_book



@router.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book_data: schemas.BookUpdate, db: Session = Depends(get_db)):
    db_book = book.get_book(db, book_id)  # ✅ fixed from book_crud to book
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book.update_book(db, book_id=book_id, book_update=book_data)  # ✅ fixed book_crud and param name
