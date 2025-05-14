import requests
from fastapi import FastAPI

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/legal/")
def generate_legal(text: str):
    payload = {
        "model": 'deepseek-r1',
        "prompt": f"Generate a legal document:\n\n{text}",
        "stream": False,
    }

    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No contract generated.")