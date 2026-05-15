from utils.jwt_handler import create_access_token

def login_user(username:str,password:str):
    if username=="admin" and password=="1234":
        token=create_access_token(
            {
                "sub": username
            }
        )
        return {
            "access_token": token,
            "token_type": "bearer"
        }
    return {
        "error": "Invalid username or password"
    }   