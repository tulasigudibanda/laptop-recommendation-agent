from fastapi import FastAPI
from pydantic import BaseModel

from agent import ask_agent

app = FastAPI()


class ChatRequest(BaseModel):
    messages: list


@app.post("/chat")
def chat(request: ChatRequest):

    answer = ask_agent(request.messages)

    return {"answer": answer}
