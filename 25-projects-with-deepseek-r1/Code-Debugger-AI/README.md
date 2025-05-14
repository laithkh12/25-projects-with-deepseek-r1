
# AI-Powered Code Debugger

## Overview
The **AI-Powered Code Debugger** is a Python-based application that uses the DeepSeek AI model to debug and analyze code. It identifies issues in the provided code, suggests fixes, and provides explanations for the corrections. The project includes two main components: an API service built with FastAPI and a user-friendly web interface using Gradio. This application supports multiple programming languages like Python, JavaScript, Java, and C++.

## Features
- **Code Debugging:** Automatically identifies bugs in the provided code and suggests fixes.
- **Code Explanation:** Provides explanations for the debugging suggestions.
- **Supports Multiple Languages:** Works with Python, JavaScript, Java, and C++.
- **Web Interface:** A simple Gradio interface where users can input buggy code and receive AI-generated debugging suggestions.

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
python code_debugger.py
```
The Gradio interface will open in your browser. You can now input buggy code, select the language, and receive AI debugging suggestions.

## File Descriptions

### `app.py`
The FastAPI backend application that exposes a POST endpoint `/debug_code/` for debugging code. It sends the buggy code to the DeepSeek AI model and returns the AI-generated debugging output, including fixes and explanations.

#### Key Components:
- FastAPI for handling API requests.
- Uses the `requests` library to communicate with the DeepSeek AI model.

### `code_debugger.py`
A script that creates a Gradio-based web interface for interacting with the AI model. Users can paste buggy code into the interface, select the programming language, and the application will return AI-generated debugging suggestions.

#### Key Components:
- Uses the `requests` library to interact with the DeepSeek API.
- Gradio is used for creating the user interface.
- Supports multiple programming languages (Python, JavaScript, Java, C++).

## Usage

1. **API Usage (FastAPI):**
   - POST your buggy code to `http://127.0.0.1:8000/debug_code/`.
   - Example payload:
     ```json
     {
       "code_snippet": "def add_numbers(a, b): return a + b
print(add_numbers(5))"
     }
     ```
   - The response will contain the AI-generated debugging output.

2. **Web Interface (Gradio):**
   - Paste your buggy code into the Gradio interface.
   - Select the programming language.
   - The app will display the AI-generated debugging output with explanations and fixes.

## Example

### Sample Buggy Code:
```python
def add_numbers(a, b):
    return a + b
print(add_numbers(5))
```

### AI Debugging Output:
- **Error:** The function `add_numbers()` requires two arguments, but only one is passed during the function call.
- **Suggested Fix:** Add the second argument to the function call:
```python
print(add_numbers(5, 3))
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
