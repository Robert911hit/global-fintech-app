# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.auth import auth_router
from app.routes.transactions import transaction_router
from app.routes.ai import ai_router

app = FastAPI()

# Enable CORS (frontend can call backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set specific frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount routes
app.include_router(auth_router, prefix="/auth")
app.include_router(transaction_router, prefix="/transactions")
app.include_router(ai_router, prefix="/ai")

@app.get("/")
def home():
    return {"message": 
