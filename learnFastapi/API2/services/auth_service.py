def loginUser(username:str,password:str):
    if username=="admin" and password=="abcd1234":
        return f"welcome {username}"
    return "invalid creds"