import requests
from fastapi import FastAPI

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/recommend/")
def recommend_products(query:str):
    payload = {
        "model": "deepseek-r1",
        "prompt": f"Recommended products:\n\n{query}",
        "stream": False,
    }

    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No recommendation avaliable.")