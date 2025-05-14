import requests
import gradio as gr

OLLAMA_URL = "http://localhost:11434/api/generate"

def analyze_symptom(symptoms):
    prompt = f"Analyze the following symptoms and suggest possible health conditions:\n\nSymptoms: {symptoms}\n\n" \
             "Provide a short list of possible causes and general adive (no treatment recommendations)."
    
    # prompt = f"Analyze the following symptoms and classify them as mild, moderate, or severe:\n\nSymptoms: {symptoms}"
    # prompt = f"Analyze symptoms in {language} and provide a response:\n\nSymptoms: {symptoms}"
    
    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False,
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200 :
        return response.json().get("response", "No information avaliable.")
    else:
        return f"Error: {response.text}"
    
interface = gr.Interface(
    fn=analyze_symptom,
    inputs=gr.Textbox(lines=2, placehold="Enter your symptoms (e.g., fever, cough, sore throat)"),
    outputs=gr.Textbox(label="Possible Conditions and Advice"),
    title="AI Medical Stmptom Checker",
    description="Enter your symptoms, and the AI will suggest possible causes and general advice."
)

if __name__ == "__main__":
    interface.launch()