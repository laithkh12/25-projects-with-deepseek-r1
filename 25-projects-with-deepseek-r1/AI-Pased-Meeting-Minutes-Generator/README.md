
# AI-Powered Meeting Minutes Generator

## Overview
The **AI-Powered Meeting Minutes Generator** is a Python-based application that uses the DeepSeek AI model to automatically generate structured meeting minutes from a transcript. It can process meeting discussions, extract key points, decisions made, and action items. The project includes two main components: an API service built with FastAPI and a web interface using Gradio. The application can also transcribe meeting audio files into text, allowing users to generate minutes from audio.

## Features
- **Meeting Transcript Analysis:** Automatically generates structured meeting minutes, summarizing discussions, decisions, and action items.
- **Audio Transcription:** Supports transcription of meeting audio into text for minute generation.
- **Web Interface:** A simple Gradio interface that allows users to input transcripts and get AI-generated minutes.
  
## Requirements
- Python 3.7 or higher
- FastAPI
- Uvicorn (for running the FastAPI app)
- Gradio
- Requests
- SpeechRecognition (for audio transcription)
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
python meeting_minutes.py
```
The Gradio interface will open in your browser. You can now input a meeting transcript or upload an audio file to generate the meeting minutes.

## File Descriptions

### `app.py`
The FastAPI backend application that exposes a POST endpoint `/meeting_minutes/` for generating meeting minutes. It sends the meeting transcript to the DeepSeek AI model and returns the AI-generated summary.

#### Key Components:
- FastAPI for handling API requests.
- Uses the `requests` library to communicate with the DeepSeek AI model.

### `meeting_minutes.py`
A script that creates a Gradio-based web interface for interacting with the AI model. Users can paste a meeting transcript, and the application will generate a structured summary of the meeting, including key points, decisions, and action items. It also provides functionality to transcribe audio files into text.

#### Key Components:
- Uses the `requests` library to interact with the DeepSeek API.
- Gradio is used for creating the user interface.
- SpeechRecognition is used for audio transcription.

## Usage

1. **API Usage (FastAPI):**
   - POST your meeting transcript to `http://127.0.0.1:8000/meeting_minutes/`.
   - Example payload:
     ```json
     {
       "transcript": "John: Q4 sales increased by 15%. Sarah: We need to increase the marketing budget. Decision: Approve higher budget."
     }
     ```
   - The response will contain the AI-generated meeting minutes.

2. **Web Interface (Gradio):**
   - Paste your meeting transcript into the Gradio interface.
   - The app will display the AI-generated meeting minutes with key discussions, decisions, and action items.
   - You can also upload audio files for transcription into text.

## Example

### Sample Transcript:
"John: Q4 sales increased by 15%. Sarah: We need to increase the marketing budget. Decision: Approve higher budget."

### AI-Generated Meeting Minutes:
- **Key Discussion:** Sales increased by 15% in Q4.
- **Decision:** Approve increased marketing budget.
- **Action Items:** Increase marketing budget for Q1.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
