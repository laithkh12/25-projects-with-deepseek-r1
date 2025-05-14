import requests
import fastapi as FastAPI

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post('/analyze_sentiment/')
def analyze_sentiment(text:str):
    payload = {
        "model": "deepseek-r1",
        "prompt": f"Classify sentiment:\n\n{text}",
        "stream": False,
    }
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No sentiment generated")