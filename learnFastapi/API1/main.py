from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def home():
    return {"message":"Hello World"}

@app.get("/search")
def search(query:str):
    return f'you searched for {query}'

@app.get("/user/{name}")
def user(name:str):
    return {"username":name}



class loginRequest(BaseModel):
    username:str
    password:int
@app.post("/login")
def login(data:loginRequest):
    return f"{data.username} logged in successfully"