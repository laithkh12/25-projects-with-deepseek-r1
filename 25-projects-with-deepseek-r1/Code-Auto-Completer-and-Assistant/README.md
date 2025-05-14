
# AI-Powered Code Auto-Completer and Assistant

## Overview
The **AI-Powered Code Auto-Completer and Assistant** is a Python-based application that uses the DeepSeek AI model to complete incomplete code snippets and debug existing code. The project includes two main components: an API service built with FastAPI and a user-friendly web interface using Gradio. The application assists developers by providing code completions, optimizations, and suggestions for various programming languages such as Python, JavaScript, Java, and C++.

## Features
- **Code Completion:** Automatically completes incomplete code snippets based on user input.
- **Code Debugging and Optimization:** Suggests fixes and improvements for existing code.
- **Supports Multiple Languages:** Works with Python, JavaScript, Java, and C++.
- **Web Interface:** A simple Gradio interface where users can input incomplete code or code to be debugged and receive AI-generated suggestions.

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
python code_autocompleter.py
```
The Gradio interface will open in your browser. You can now enter incomplete code or code that needs debugging and receive AI suggestions.

## File Descriptions

### `app.py`
The FastAPI backend application that exposes a POST endpoint `/complete_code/` for code completion. It sends the code snippet to the DeepSeek AI model and returns the AI-generated code completion.

#### Key Components:
- FastAPI for handling API requests.
- Uses the `requests` library to communicate with the DeepSeek AI model.

### `code_autocompleter.py`
A script that creates a Gradio-based web interface for interacting with the AI model. Users can paste an incomplete code snippet and select the language, and the application will provide AI-generated code completions.

#### Key Components:
- Uses the `requests` library to interact with the DeepSeek API.
- Gradio is used for creating the user interface.
- Supports multiple programming languages (Python, JavaScript, Java, C++).

## Usage

1. **API Usage (FastAPI):**
   - POST your incomplete code to `http://127.0.0.1:8000/complete_code/`.
   - Example payload:
     ```json
     {
       "code_snippet": "def fibonacci(n):",
       "language": "Python"
     }
     ```
   - The response will contain the AI-generated code completion.

2. **Web Interface (Gradio):**
   - Paste your incomplete code snippet into the Gradio interface.
   - Select the programming language.
   - The app will display the AI-generated code completion or debugging suggestion.

## Example

### Sample Code:
```python
def fibonacci(n):
```

### AI-Suggested Code Completion:
```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
