from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

auth_router = APIRouter()

# Fake user database (for now)
users_db = {}

class AuthRequest(BaseModel):
    email: str
    password: str

@auth_router.post("/signup")
def signup(data: AuthRequest):
    if data.email in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[data.email] = {"password": data.password, "balance": 0.0}
    return {"message": "User created successfully"}

@auth_router.post("/login")
def login(data: AuthRequest):
    user = users_db.get(data.email)
    if not user or user["password"] != data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}
