import requests
import gradio as gr

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_email_response(email_content, tone="Formal"):
    prompt = f"Generate an {tone} email as a response from the customer support team to the customer for the following email:\n\n{email_content}\n\n" \
    f"Ensure the response is polite, clear, and profissional."

    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False,
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200 :
        return response.json().get("response", "No response generated")
    else:
        return f"Error: {response.text}"

interface = gr.Interface(
    fn=generate_email_response,
    inputs=[
        gr.Textbox(lines=5, placeholder='Paste the email content here.'),
        gr.Radio(["Formal", "Casual", "Friendly"], label="Tone"),
    ],
    outputs=gr.Textbox(label="AI-Genrated Email Response."),
    title="AI-Powered Email Responder",
    description="Paste an email and let AI generate a profissional response."
)

if __name__ == "__main__":
    interface.launch()