from fastapi import APIRouter
from pydantic import BaseModel
import openai
import os

ai_router = APIRouter()

# Load your GPT-4 API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

class AIRequest(BaseModel):
    message: str

@ai_router.post("/ask")
def ask_ai(req: AIRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": req.message}],
        )
        return {"reply": response['choices'][0]['message']['content']}
    except Exception as e:
        return {"error": str(e)}
