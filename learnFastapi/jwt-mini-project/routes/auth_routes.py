from fastapi import APIRouter, Header, HTTPException
from schemas.auth_schema import userLogin
from services.auth_services import login_user
from utils.jwt_handler import verify_access_token

router = APIRouter()

@router.post('/login')
def login(data: userLogin):
    return login_user(
        data.username,
        data.password
    )

@router.get('/me')
def get_me(authorization: str = Header(None)):

    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Authorization header missing"
        )

    token = authorization.split(" ")[1]

    username = verify_access_token(token)

    if not username:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    return {
        "username": username,
        "message": "Protected profile access granted"
    }