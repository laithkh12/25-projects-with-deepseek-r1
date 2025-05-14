
# AI-Powered Medical Symptom Checker

## Overview
The **AI-Powered Medical Symptom Checker** is a Python-based application that uses the DeepSeek AI model to analyze symptoms and suggest possible health conditions. The project includes two main components: an API service built with FastAPI and a user-friendly web interface using Gradio. This tool is designed to assist individuals by providing possible causes and general advice based on their symptoms (without offering treatment recommendations).

## Features
- **Symptom Analysis:** Analyzes symptoms and provides a list of possible health conditions.
- **General Advice:** Provides general advice based on the analyzed symptoms.
- **Web Interface:** A simple Gradio interface to enter symptoms and receive AI-generated responses.

## Requirements
- Python 3.7 or higher
- FastAPI
- Uvicorn (for running the FastAPI app)
- Gradio
- Requests
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
python symptom_checker.py
```
The Gradio interface will open in your browser. You can now enter your symptoms and get AI-generated analysis.

## File Descriptions

### `app.py`
The FastAPI backend application that exposes a POST endpoint `/medical/` for analyzing symptoms. It sends the user's symptoms to the DeepSeek AI model and returns the AI-generated analysis, including possible health conditions and general advice.

#### Key Components:
- FastAPI for handling API requests.
- Uses the `requests` library to communicate with the DeepSeek AI model.

### `symptom_checker.py`
A script that creates a Gradio-based web interface for interacting with the AI-powered symptom checker. Users can enter their symptoms into the Gradio interface, and the app will return the AI-generated analysis.

#### Key Components:
- Uses the `requests` library to interact with the DeepSeek API.
- Gradio is used for creating the user interface.

## Usage

1. **API Usage (FastAPI):**
   - POST your symptoms to `http://127.0.0.1:8000/medical/`.
   - Example payload:
     ```json
     {
       "symptoms": "fever, cough, sore throat"
     }
     ```
   - The response will contain the AI-generated analysis of possible health conditions.

2. **Web Interface (Gradio):**
   - Enter your symptoms into the Gradio interface.
   - The app will display the AI-generated analysis and general advice.

## Example

### Sample Symptoms:
"fever, cough, sore throat"

### AI-Generated Response:
- **Possible Conditions:** Flu, Cold, COVID-19
- **General Advice:** Rest, drink plenty of fluids, and monitor your symptoms. If the symptoms persist or worsen, consider seeing a healthcare provider.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
