
# AI-Powered Personal Assistant

## Overview
The **AI-Powered Personal Assistant** is a Python-based application that uses the DeepSeek AI model to provide conversational responses to user queries. The project includes two main components: an API service built with FastAPI and a user-friendly web interface using Gradio. The assistant can respond to typed queries and provide voice-based interactions using speech recognition and text-to-speech.

## Features
- **Text and Voice Interaction:** Users can interact with the assistant through text or voice commands.
- **Speech Recognition and Text-to-Speech:** The assistant can listen to voice commands and respond with speech.
- **Web Interface:** A simple Gradio interface for text-based interactions with the assistant.
- **AI-Powered Responses:** The assistant generates intelligent responses based on user queries using the DeepSeek AI model.

## Requirements
- Python 3.7 or higher
- FastAPI
- Uvicorn (for running the FastAPI app)
- Gradio
- Requests
- SpeechRecognition (for speech-to-text)
- pyttsx3 (for text-to-speech)
- DeepSeek AI model

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/laithkh12/25-projects-with-deepseek-r1.git
cd 25-projects-with-deepseek-r1
```

### 2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Start the FastAPI app (API Service):
```bash
uvicorn app:app --reload
```
This will start the API server locally at `http://127.0.0.1:8000`.

### 4. Launch the Gradio web interface:
```bash
python ai_assistant.py
```
The Gradio interface will open in your browser. You can now type or speak your queries, and the assistant will respond.

## File Descriptions

### `app.py`
The FastAPI backend application that exposes a POST endpoint `/assistant/` for handling user queries. It sends the user's query to the DeepSeek AI model and returns the AI-generated response.

#### Key Components:
- FastAPI for handling API requests.
- Uses the `requests` library to communicate with the DeepSeek AI model.

### `ai_assistant.py`
A script that creates a Gradio-based web interface for interacting with the AI-powered assistant. Users can type their queries, and the assistant will respond with AI-generated text. The assistant can also listen to voice commands and speak its responses using speech recognition and text-to-speech.

#### Key Components:
- Uses the `requests` library to interact with the DeepSeek API.
- Gradio is used for creating the user interface.
- SpeechRecognition is used for converting speech to text.
- pyttsx3 is used for text-to-speech functionality.

## Usage

1. **API Usage (FastAPI):**
   - POST your query to `http://127.0.0.1:8000/assistant/`.
   - Example payload:
     ```json
     {
       "text": "Tell me a fun fact about space."
     }
     ```
   - The response will contain the AI-generated response from the assistant.

2. **Web Interface (Gradio):**
   - Enter your query in the Gradio interface, or use your microphone to speak.
   - The app will display the AI-generated response in text and speak the response aloud.

## Example

### Sample Query:
"Tell me a fun fact about space."

### AI Assistant Response:
"Did you know that space is completely silent? There is no air in space to carry sound, so astronauts use radios to communicate."

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
