import requests
import gradio as gr

OLLAMA_URL = "http://localhost:11434/api/generate"

def analyze_sentiment(text):
    prompt = f"Classify the sentiment of the follwoing text as Positive, Negative, or Neutral:\n\n{text}"

    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False,
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No sentiment generated")
    else:
        return f"Error: {response.text}"
    
interface = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(lines=3, placeholder="Enter a sentence for sentiment analysis"),
    outputs=gr.Textbox(label="Sentiment Result"),
    title="AI-Powered Sentiment Analysis",
    description="Enter a sentence, and DeepSeek AI will classify its sentiment as Positive, Negative, or Neutral."
)

if __name__ == "__main__":
    interface.launch()
    
# if __name__ == "__main__":
#     sample_text = "The movie was absolutely fantastic! I enjoyed every minute of it."
#     print("### Sentiment Analysis Result ###")
#     print(analyze_sentiment(sample_text))