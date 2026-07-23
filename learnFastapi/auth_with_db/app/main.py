from fastapi import FastAPI

try:
    from .database.db import engine
    from .database.models import Base
except ImportError:  # pragma: no cover - support direct script execution
    from database.db import engine
    from database.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Authentication Service"
    }