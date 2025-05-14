
# AI-Powered Grammar and Spell Checker

## Overview
The **AI-Powered Grammar and Spell Checker** is a Python-based application that uses the DeepSeek AI model to automatically correct grammar and spelling mistakes in user-provided text. The project includes two main components: an API service built with FastAPI and a user-friendly web interface using Gradio. This application can be used for proofreading and improving the quality of written content.

## Features
- **Grammar and Spell Check:** Automatically corrects grammar and spelling mistakes in text.
- **Text Input:** Users can input text with errors, and the AI will provide a corrected version.
- **Web Interface:** A simple Gradio interface that allows users to enter text with errors and get AI-generated corrections.

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
python grammer_checker.py
```
The Gradio interface will open in your browser. You can now enter text with grammar or spelling mistakes, and the app will provide a corrected version.

## File Descriptions

### `app.py`
The FastAPI backend application that exposes a POST endpoint `/correct/` for grammar and spelling correction. It sends the provided text to the DeepSeek AI model and returns the corrected text.

#### Key Components:
- FastAPI for handling API requests.
- Uses the `requests` library to communicate with the DeepSeek AI model.

### `grammer_checker.py`
A script that creates a Gradio-based web interface for interacting with the AI model. Users can input text with grammar or spelling mistakes, and the application will return the corrected text.

#### Key Components:
- Uses the `requests` library to interact with the DeepSeek API.
- Gradio is used for creating the user interface.
- Provides a simple interface for text correction.

## Usage

1. **API Usage (FastAPI):**
   - POST your text with grammar or spelling mistakes to `http://127.0.0.1:8000/correct/`.
   - Example payload:
     ```json
     {
       "text": "He dont like to eat apple because they taste sour."
     }
     ```
   - The response will contain the AI-generated corrected text.

2. **Web Interface (Gradio):**
   - Enter your text with grammar or spelling mistakes into the Gradio interface.
   - The app will display the corrected text.

## Example

### Sample Text:
"He dont like to eat apple because they taste sour."

### AI-Generated Corrected Text:
"He doesn't like to eat apples because they taste sour."

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
