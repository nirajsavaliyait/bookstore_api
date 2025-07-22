from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index= True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    book = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index= True)
    title = Column(String, index=True)
    description = Column(String)

    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates="book")

