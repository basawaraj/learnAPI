from fastapi import FastAPI

from .database.db import engine
from .database.models import Base
from .routes.student_routes import router as student_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(student_router)


@app.get("/")
def home():
    return {"message": "Welcome to student API!"}
 