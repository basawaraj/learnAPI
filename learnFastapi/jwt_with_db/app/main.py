from fastapi import FastAPI

from .database.db import engine
from .database.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to student API!"}
 