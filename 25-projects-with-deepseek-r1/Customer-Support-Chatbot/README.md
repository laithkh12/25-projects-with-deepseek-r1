
# AI-Powered Customer Support Chatbot

## Overview
The **AI-Powered Customer Support Chatbot** is a Python-based application that uses the DeepSeek AI model to respond to customer queries by matching them with the most relevant answers from a pre-defined FAQ database. The project includes two main components: an API service built with FastAPI and a user-friendly web interface using Gradio. The application can answer customer questions based on a set of frequently asked questions (FAQs).

## Features
- **AI-Powered Responses:** Responds to customer queries using AI, by matching them with relevant FAQ entries.
- **FAQ Database:** Contains a set of commonly asked questions and their answers, such as order tracking, return policies, payment methods, and more.
- **Web Interface:** A simple Gradio interface that allows users to ask questions and receive AI-generated answers from the FAQ database.

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
python customer_support_bot.py
```
The Gradio interface will open in your browser. You can now ask customer support questions, and the chatbot will provide the best-matching FAQ answer.

## File Descriptions

### `app.py`
The FastAPI backend application that exposes a POST endpoint `/chatbot/` for responding to customer queries. It sends the query to the DeepSeek AI model and returns the best matching response from the FAQ database.

#### Key Components:
- FastAPI for handling API requests.
- Uses the `requests` library to communicate with the DeepSeek AI model.

### `customer_support_bot.py`
A script that creates a Gradio-based web interface for interacting with the AI-powered chatbot. Users can input their queries into the Gradio interface, and the app will return the best-matching answer from the FAQ database.

#### Key Components:
- Uses the `requests` library to interact with the DeepSeek API.
- Gradio is used for creating the user interface.
- Predefined FAQ database for matching customer queries.

## Usage

1. **API Usage (FastAPI):**
   - POST your customer query to `http://127.0.0.1:8000/chatbot/`.
   - Example payload:
     ```json
     {
       "query": "How can I return a product?"
     }
     ```
   - The response will contain the best matching answer from the FAQ database.

2. **Web Interface (Gradio):**
   - Enter your customer query into the Gradio interface.
   - The app will display the AI-generated response based on the FAQ database.

## Example

### Sample Customer Query:
"How can I return a product?"

### AI-Generated Response:
"You can return your product by logging into your account and visiting the Returns page. We accept returns within 30 days."

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
