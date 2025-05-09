from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests
from pydantic import BaseModel

class req(BaseModel):
    prompt :str

app = FastAPI()

# Allow frontend origin (adjust port if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/chat")
async def chat(prompt: req):

    instruction = (
        "You are an AI trained to return a single word, nothing else, not even explanation or other texts just a single word. "
        "Given the following text, return only the next word.\n\n"
        f"Text: {prompt}"
    )
    url = "https://api.groq.com/openai/v1/chat/completions"
    API_KEY = "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"
    headers = {
        "Authorization":f"Bearer {API_KEY}",
        "Content-Type":"application/json"
    }
    data = {
        "messages":[{"role":"user","content":instruction}],
        "model":"meta-llama/llama-4-scout-17b-16e-instruct",
        "max_tokens": 1024
    }

    res = requests.post(url, headers=headers, json = data)

    return res.json()
