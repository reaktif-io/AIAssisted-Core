import gpt_2_simple as gpt2
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# Run tensorflow model server
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

# Run API server
app = FastAPI()


# Interfaces
class Requested(BaseModel):
    language: str
    code: str


class Suggestion(BaseModel):
    suggestions: str


# Endpoints
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/suggestion/")
async def create_suggestion(item: Requested) -> Suggestion:

    single_text = gpt2.generate(
        sess, length=len(item.code), prefix=f"{item.code}", nsamples=5, return_as_list=True, top_k=2, batch_size=5)

    return {"suggestions": single_text}
