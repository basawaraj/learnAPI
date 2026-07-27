from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.database.models import User
from app.services.auth_service import register_user, login_user
from app.schemas.auth_schema import RegisterRequest, LoginRequest

router = APIRouter()

@router.post("/register")
def register(user: RegisterRequest, db: Session=Depends(get_db)):
    try:
        new_user = register_user(db, user)
        return {"message": "User registered successfully", "user": {"id": new_user.id, "username": new_user.username, "email": new_user.email}}
    except ValueError as e:
        return {"error": str(e)}
@router.post("/login")
def login(user: LoginRequest, db: Session=Depends(get_db)):
    result = login_user(db, user)
    return result