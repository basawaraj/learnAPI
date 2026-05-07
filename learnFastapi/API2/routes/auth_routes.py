from fastapi import APIRouter
from schema.auth_schema import LoginRequest, RegisterRequest
from services.auth_service import login_user, register_user

router = APIRouter()

@router.post("/login")

def login(data:LoginRequest):
    result = login_user(data.username, data.password)
    return result


@router.post("/register")

def register(data: RegisterRequest):
    result= register_user(data.username)
    return result