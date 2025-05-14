
# AI-Powered Real-Time News Summarizer

## Overview
The **AI-Powered Real-Time News Summarizer** is a Python-based application that uses the DeepSeek AI model to summarize the latest news articles in real-time. The project includes two main components: an API service built with FastAPI and a user-friendly web interface using Gradio. The application fetches the latest news articles from a specified category (e.g., technology, business, health) and provides a short and informative summary using AI.

## Features
- **Real-Time News Fetching:** Fetches the latest news articles based on category (e.g., technology, business).
- **AI-Powered Summarization:** Summarizes news articles to provide a quick overview.
- **Web Interface:** A simple Gradio interface to select a news category and get an AI-generated summary.

## Requirements
- Python 3.7 or higher
- FastAPI
- Uvicorn (for running the FastAPI app)
- Gradio
- Requests
- DeepSeek AI model
- NewsAPI key for fetching news articles

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

### 3. Get your NewsAPI key:
- Sign up on [NewsAPI](https://newsapi.org/) and get your free API key.
- Replace the `NEWS_API_KEY` in `news_summarizer.py` with your API key.

### 4. Launch the FastAPI app (API Service):
```bash
uvicorn app:app --reload
```
This will start the API server locally at `http://127.0.0.1:8000`.

### 5. Launch the Gradio web interface:
```bash
python news_summarizer.py
```
The Gradio interface will open in your browser. You can now select a news category and get the AI-generated summary.

## File Descriptions

### `app.py`
The FastAPI backend application that exposes a POST endpoint `/extract_entities` for summarizing news articles. It fetches the latest news articles from NewsAPI and sends them to the DeepSeek AI model for summarization.

#### Key Components:
- FastAPI for handling API requests.
- Uses the `requests` library to communicate with the DeepSeek AI model and NewsAPI.

### `news_summarizer.py`
A script that creates a Gradio-based web interface for interacting with the AI-powered news summarizer. Users can select a news category, and the app will fetch and summarize the latest news articles.

#### Key Components:
- Uses the `requests` library to interact with the DeepSeek API and NewsAPI.
- Gradio is used for creating the user interface.
- Fetches news from categories like technology, business, health, and more.

## Usage

1. **API Usage (FastAPI):**
   - POST your selected category to `http://127.0.0.1:8000/extract_entities`.
   - Example payload:
     ```json
     {
       "category": "technology"
     }
     ```
   - The response will contain the AI-generated news summary.

2. **Web Interface (Gradio):**
   - Select a news category from the dropdown in the Gradio interface.
   - The app will fetch and summarize the latest news article in that category.

## Example

### Selected Category:
"Technology"

### AI-Generated News Summary:
- **Title:** "The Rise of AI in Healthcare"
- **Summary:** "AI is revolutionizing healthcare by enabling faster diagnoses, personalized treatments, and improved patient outcomes. Leading companies are investing in AI-driven healthcare solutions to enhance care delivery."

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
