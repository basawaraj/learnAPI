from fastapi import FastAPI

from app.routes.auth_routes import router as auth_router
from app.database.db import engine
from app.database.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)


@app.get("/")
def home():
    return {"message": "Authentication Service"}