
from pydantic import BaseModel
from typing import List, Optional

class Bookbase(BaseModel):
    title : str
    description : str


class BookCreate(Bookbase):
    pass 

class Book(Bookbase):
    id: int
    author_id: int

    class Config:
        from_attributes = True

class BookUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    author_id: int | None = None
# -------------------------------------------------------------------------------------------------------

class Authorbase(BaseModel):
    name : str
    email : str

class AuthorCreate(Authorbase):
    pass 

class Author(Authorbase):
    id: int
    books : List[Book] = []

    class Config:
        from_attributes = True

