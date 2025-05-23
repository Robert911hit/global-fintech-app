from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

transaction_router = APIRouter()

class Transaction(BaseModel):
    sender: str
    receiver: str
    amount: float

@transaction_router.post("/send")
def send_money(tx: Transaction):
    # In real app, you'd update DB here
    if tx.sender == tx.receiver:
        raise HTTPException(status_code=400, detail="Cannot send to self")
    if tx.amount <= 0:
        raise HTTPException(status_code=400, detail="Invalid amount")
    
    # Just a dummy return for now
    return {
        "message": f"{tx.amount} sent from {tx.sender} to {tx.receiver} 💸"
    }
