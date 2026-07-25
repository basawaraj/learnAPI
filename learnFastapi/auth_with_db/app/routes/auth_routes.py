from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .database.db import get_db
from .database.models import User
from .services.auth_service import register_user
from .schemas.auth_schemas import RegisterRequest

router = APIRouter()

@router.post("/register")
def register(user: RegisterRequest, db: Session=Depends(get_db)):
    try:
        new_user = register_user(db, user)
        return {"message": "User registered successfully", "user": {"id": new_user.id, "username": new_user.username, "email": new_user.email}}
    except ValueError as e:
        return {"error": str(e)}