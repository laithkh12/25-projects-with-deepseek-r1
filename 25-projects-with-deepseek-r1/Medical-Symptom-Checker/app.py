import requests
from fastapi import FastAPI

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post('/medical/')
def analyze_symptoms(symptoms:str):
    payload = {
        "model": "deepseek-r1",
        "prompt": f"Medical symptom analyzsis:\n\n{symptoms}",
        "stream": False,
    }

    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No info avaliable.")