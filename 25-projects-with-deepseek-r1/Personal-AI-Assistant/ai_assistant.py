import requests
import gradio as gr
import speech_recognition as sr
import pyttsx3

OLLAMA_URL = "http://localhost:11434/api/generate"

engine = pyttsx3.init()

def ai_assistant(text):
    prompt = f"Respond to this query as a personal AI assistant:\n\n{text}"

    # prompt = f"Act as a personal AI assistant. If the user asks for something, getch the data."

    # prompt = f"Respond in {language}:\n\n{text}"

    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False,
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        ai_response = response.json().get("response", "I'm sorry, I don't have an answer for that.")

        engine.say(ai_response)
        engine.runAndWait()

        return ai_response
    else: 
        return "Sorry, I couldn't process your request."
    
def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio)
        print(f"User: {command}")
        return command
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand that."
    except sr.RequestError:
        return "Speech recognition service is unavaliable."
    
interface = gr.Interface(
    fn=ai_assistant,
    inputs=gr.Textbox(lines=3, placeholder="Ask anything..."),
    outputs="text",
    title="AI-Powered Personal Assisant",
    description="Type a query or use voice commands to interact with the assistant.",
    live=True
)

if __name__ == "__main__":
    interface.launch()

# while True:
#     command = listen_command()
#     if "hey_ai" in command.lower():
#         response = ai_assistant(command)
#         print(response)
    
# if __name__ == "__main__":
#     sample_query = "Tell me a fun fact about space."
#     print("### AI Assistant Response ###")
#     print(ai_assistant(sample_query))