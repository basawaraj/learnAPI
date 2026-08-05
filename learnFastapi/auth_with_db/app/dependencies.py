from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.databse.db import get_db
from app.database.models import User
from app.utils.jwt_handler import verify_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth2_scheme), db=Depends(get_db)):
    email = verify_access_token(token)
    if email is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user