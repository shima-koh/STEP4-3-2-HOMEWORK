from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextData(BaseModel):
    text: str

@app.post("/count_characters")
def count_characters(text_data: TextData):
    characters = len(text_data.text)
    return {"character_count": characters}
