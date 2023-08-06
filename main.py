from typing import Union
from chat import get_response

from fastapi import Response, FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict")
def predict(message):
    response = get_response(message)
    msg = {"answer": response}
    return msg