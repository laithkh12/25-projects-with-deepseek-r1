import requests
from fastapi import FastAPI

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"


@app.post("/assistant/")
def ai_assistant(text: str):
    payload = {
        "model": "deepseek-r1",
        "prompt": f"AI assistant response:\n\n{text}",
        "stream": False,
    }

    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No answer avaliable.")