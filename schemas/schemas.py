
from pydantic import BaseModel, EmailStr, constr
from typing import List, Optional
from typing import Annotated

class Bookbase(BaseModel):
    title : Annotated[str, constr(min_length=1, max_length=100)]
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
    name : Annotated[str,constr(min_length=3)]
    email : EmailStr

class AuthorCreate(Authorbase):
    pass 

class Author(Authorbase):
    id: int
    books : List[Book] = []

    class Config:
        from_attributes = True

