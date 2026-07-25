from sqlalchemy.orm import Session

from .database.models import User
from .utils.password_handler import hash_password, verify_password

def register_user(db: Session, user):

    existing_user = db.query(User).filter((User.email == user.email) | (User.username == user.username)).first()
    if existing_user:
        raise ValueError("User with this email or username already exists.")
    
    existing_email = db.query(User).filter(User.email == user.email).first()
    if existing_email:
        raise ValueError("User with this email already exists.")
    new_user = User(
        email=user.email,
        username=user.username,
        hashed_password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit() 
    db.refresh(new_user)
    return new_user
