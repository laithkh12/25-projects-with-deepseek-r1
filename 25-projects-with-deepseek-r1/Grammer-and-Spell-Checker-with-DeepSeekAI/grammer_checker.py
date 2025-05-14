import requests
import gradio as gr

OLLAMA_URL = "http://localhost:11434/api/generate"

def correct_grammer(text):
    prompt = f"Correct and spelling and grammer mistakes in the following text:\n\n{text}"

    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False,
    }

    response = requests.post(OLLAMA_URL, json=payload)
    
    if response.status_code == 200:
        return response.json().get("response", "No correction generated")
    else:
        return f"Error: {response.text}"

interface = gr.Interface(
    fn=correct_grammer,
    inputs=gr.Textbox(lines=5, placeholder="Enter text with grammer or spelling mistakes"),
    outputs=gr.Textbox(label="Corrected Text"),
    title="AI-Powered Grammer and Spell Checker",
    description="Enter text with errors, and DeepSeek AI will correct them"
)

if __name__ == "__main__":
    interface.launch()

# if __name__ == "__main__":
#     sample_text = "He dont like to eat apple because they taste sour."
#     print("### Corrected Text ###")
#     print(correct_grammer(sample_text))