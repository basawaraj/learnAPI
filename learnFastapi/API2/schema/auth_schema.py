from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str


## when we have 2 vars declared we cant only use 1
class RegisterRequest(BaseModel):
    username: str