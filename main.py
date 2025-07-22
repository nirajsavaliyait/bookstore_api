from fastapi import FastAPI
from models import models
from database.database import engine
from routers import routes


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(routes.router)

@app.get("/")  # for rendering 
def read_root():
    return {"message": "Welcome to the Bookstore API"}