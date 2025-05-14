from fastapi import FastAPI
import requests

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/extract_entities")
def extraced_names_entities(text:str):
    payload = {
        "model": "deepseek-r1",
        "prompt": f"Extract entities:\n\n{text}",
        "stream": False,
    }

    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No entities generated")