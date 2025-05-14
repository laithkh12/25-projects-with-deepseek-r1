
# AI-Powered Text Generation

## Overview
The **AI-Powered Text Generation** is a Python-based application that uses the DeepSeek AI model to generate text based on a given prompt. Users can input a prompt, specify a word limit, and the AI will generate coherent text within the word limit. The project consists of two main components: an API service built with FastAPI and a user-friendly web interface using Gradio. This app is useful for content generation, article writing, and brainstorming.

## Features
- **Text Generation:** Generate text based on a user-provided prompt.
- **Word Limit:** Specify a word limit for the generated text (default is 100 words).
- **Web Interface:** A simple Gradio interface to enter a prompt and select the word limit for text generation.

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
python text_generator.py
```
The Gradio interface will open in your browser. You can now enter a prompt and generate text based on the AI model.

## File Descriptions

### `app.py`
The FastAPI backend application that exposes a POST endpoint `/generate/` for generating text based on user input. It sends the provided prompt to the DeepSeek AI model and returns the generated text.

#### Key Components:
- FastAPI for handling API requests.
- Uses the `requests` library to communicate with the DeepSeek AI model.

### `text_generator.py`
A script that creates a Gradio-based web interface for interacting with the AI model. Users can enter a prompt and set a word limit for the AI-generated text.

#### Key Components:
- Uses the `requests` library to interact with the DeepSeek API.
- Gradio is used for creating the user interface.
- The app generates text based on the prompt and word limit specified by the user.

## Usage

1. **API Usage (FastAPI):**
   - POST your prompt and word limit to `http://127.0.0.1:8000/generate/`.
   - Example payload:
     ```json
     {
       "prompt": "Write an introduction for an article about the future of AI.",
       "word_limit": 150
     }
     ```
   - The response will contain the AI-generated text.

2. **Web Interface (Gradio):**
   - Enter your prompt and select the word limit in the Gradio interface.
   - The app will display the AI-generated content.

## Example

### Sample Prompt:
"Write an introduction for an article about the future of AI."

### AI-Generated Text:
The future of AI is both exciting and uncertain. As technology continues to evolve, AI is expected to transform various industries, from healthcare to finance, and revolutionize the way we interact with the world. In this article, we will explore the potential benefits and challenges of AI, as well as its impact on the workforce and society at large.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
