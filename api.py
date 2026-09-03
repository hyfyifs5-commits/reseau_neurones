from fastapi import FastAPI
from pydantic import BaseModel
from bot import repondre

app = FastAPI()

class MessageRequest(BaseModel):
    message: str

@app.post("/chat")
def chat_endpoint(request: MessageRequest):
    intention, confiance, reponse = repondre(request.message)
    return {
        "intention": intention,
        "confiance": confiance,
        "reponse": reponse
    }