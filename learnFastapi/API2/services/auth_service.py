def login_user(username: str, password: str):
    if username == "admin" and password == "123":
        return {"message": "Login success"}
    return {"error": "Invalid credentials"}

# register user
def register_user(username: str):
    return {"message": f"{username} registered successfully"}
