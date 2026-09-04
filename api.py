<<<<<<< HEAD
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
=======
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
>>>>>>> c28d3c9d8d1eb8ad704793ee4cedca9b5342313c
    }