import users
from fastapi import FastAPI, Security, HTTPException
from pydantic import BaseModel
from secure import Secure

API_KEY = "supersecretapikey"
auth = Secure(accepted_keys=[API_KEY])

app = FastAPI()

class User(BaseModel):
    username: str
    email: str
    password: str

class PartialUser(BaseModel):
    username: str
    password: str

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/users/")
def create_user(user: User, api_key: str = Security(auth)): 
    isValid = users.add_user(user.username, user.email, user.password)

    if isValid:
        return {"message": "User created successfully", "success": True}
    else:
        raise HTTPException(status_code=409, detail="User already exists")

@app.post("/users/login/")
def login_user(user: PartialUser, api_key: str = Security(auth)):
    isValid = users.verify_user(user.username, user.password)

    if isValid:
        return {"message": "User logged in successfully", "success": True}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")