from app.utils.jwt_handler import create_access_token
from sqlalchemy.orm import Session

from app.database.models import User
from app.utils.password_handler import hash_password, verify_password

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

def login_user(db,user):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user is None:
     return { "message": "invalid user email or password"}

    if not verify_password(user.password, db_user.hashed_password):
        return { "message": "invalid user email or password"}
    token = create_access_token({"sub": db_user.email})

    return { "message": "Login successful", "user": {"id": db_user.id, "username": db_user.username, "email": db_user.email} , "access_token": token }