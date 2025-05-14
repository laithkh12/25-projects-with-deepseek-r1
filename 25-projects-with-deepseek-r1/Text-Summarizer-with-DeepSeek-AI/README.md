
# AI-Powered Text Summarizer

## Overview
The **AI-Powered Text Summarizer** is a Python-based application that uses the DeepSeek AI model to summarize text. The project includes two main components: an API service built with FastAPI and a user-friendly web interface using Gradio. This tool is designed to help users quickly generate concise summaries for long pieces of text, making it ideal for summarizing articles, reports, or any other lengthy content.

## Features
- **Text Summarization:** Automatically summarizes long text into concise bullet points.
- **Web Interface:** A simple Gradio interface to input long text and get AI-generated summaries.
- **Customizable Summaries:** Users can generate summaries in the form of bullet points.

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
python text_summarizer.py
```
The Gradio interface will open in your browser. You can now input long text, and the app will generate a concise summary.

## File Descriptions

### `app.py`
The FastAPI backend application that exposes a POST endpoint `/summarize/` for summarizing text. It sends the provided text to the DeepSeek AI model and returns the summarized text.

#### Key Components:
- FastAPI for handling API requests.
- Uses the `requests` library to communicate with the DeepSeek AI model.

### `text_summarizer.py`
A script that creates a Gradio-based web interface for interacting with the AI-powered text summarizer. Users can input long text, and the app will return the summarized text in the form of bullet points.

#### Key Components:
- Uses the `requests` library to interact with the DeepSeek API.
- Gradio is used for creating the user interface.
- Summarizes the text into concise bullet points.

## Usage

1. **API Usage (FastAPI):**
   - POST your text to `http://127.0.0.1:8000/summarize/`.
   - Example payload:
     ```json
     {
       "text": "Artificial Intelligence is transforming industries across the world. AI models like DeepSeek-R1 enable businesses to automate tasks, analyze large datasets, and enhance productivity. With advancements in AI, applications range from virtual assistants to predictive analytics and personalized recommendations."
     }
     ```
   - The response will contain the AI-generated summary in bullet points.

2. **Web Interface (Gradio):**
   - Enter your long text into the Gradio interface.
   - The app will display the AI-generated summary.

## Example

### Sample Text:
"Artificial Intelligence is transforming industries across the world. AI models like DeepSeek-R1 enable businesses to automate tasks, analyze large datasets, and enhance productivity. With advancements in AI, applications range from virtual assistants to predictive analytics and personalized recommendations."

### AI-Generated Summary:
- AI is revolutionizing industries globally by automating tasks and analyzing large datasets.
- DeepSeek-R1 helps businesses increase productivity.
- Applications of AI include virtual assistants, predictive analytics, and personalized recommendations.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
