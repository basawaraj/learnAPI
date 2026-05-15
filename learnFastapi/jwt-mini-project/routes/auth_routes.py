from fastapi import APIRouter
from schemas.auth_schema import userLogin
from services.auth_services import login_user

router=APIRouter()

@router.post('/login')
def login(data:userLogin):
    return login_user(
        data.username,
        data.password
    )