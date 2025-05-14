
# AI-Powered Sentiment Analysis

## Overview
The **AI-Powered Sentiment Analysis** is a Python-based application that uses the DeepSeek AI model to classify the sentiment of a given text. It can determine whether the sentiment of the text is Positive, Negative, or Neutral. The project includes two main components: an API service built with FastAPI and a user-friendly web interface using Gradio. The application provides users with real-time sentiment analysis for any given sentence.

## Features
- **Sentiment Classification:** Classifies the sentiment of a text as Positive, Negative, or Neutral.
- **Real-Time Analysis:** Instant feedback on the sentiment of any given sentence.
- **Web Interface:** A simple Gradio interface for easy sentiment analysis.

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
python sentiment_analysis.py
```
The Gradio interface will open in your browser. You can now enter a sentence for sentiment analysis.

## File Descriptions

### `app.py`
The FastAPI backend application that exposes a POST endpoint `/analyze_sentiment/` for sentiment analysis. It sends the provided text to the DeepSeek AI model and returns the sentiment classification (Positive, Negative, or Neutral).

#### Key Components:
- FastAPI for handling API requests.
- Uses the `requests` library to communicate with the DeepSeek AI model.

### `sentiment_analysis.py`
A script that creates a Gradio-based web interface for interacting with the AI model. Users can input text into the Gradio interface, and the application will return the AI-generated sentiment classification.

#### Key Components:
- Uses the `requests` library to interact with the DeepSeek API.
- Gradio is used for creating the user interface.

## Usage

1. **API Usage (FastAPI):**
   - POST your text to `http://127.0.0.1:8000/analyze_sentiment/`.
   - Example payload:
     ```json
     {
       "text": "The movie was absolutely fantastic! I enjoyed every minute of it."
     }
     ```
   - The response will contain the AI-generated sentiment classification (Positive, Negative, or Neutral).

2. **Web Interface (Gradio):**
   - Enter your text in the Gradio interface.
   - The app will display the sentiment result (Positive, Negative, or Neutral).

## Example

### Sample Text:
"The movie was absolutely fantastic! I enjoyed every minute of it."

### AI-Generated Sentiment:
- **Sentiment:** Positive

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
