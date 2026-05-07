from fastapi import APIRouter
from schema.auth_schema import LoginRequest
from services.auth_service import login_user

router = APIRouter()

@router.post("/login")

def login(data:LoginRequest):
    result = login_user(data.username, data.password)
    return result
