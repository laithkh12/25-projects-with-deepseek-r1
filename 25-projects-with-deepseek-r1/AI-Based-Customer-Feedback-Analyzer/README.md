
# AI-Based Customer Feedback Analyzer

## Overview
The **AI-Based Customer Feedback Analyzer** is a Python-based application that leverages the DeepSeek AI model to analyze and extract insights from customer feedback. The project consists of two main components: an API service built with FastAPI and a web interface using Gradio. These components allow users to input customer feedback and receive sentiment analysis, key insights, and actionable recommendations based on the provided data.

## Features
- **Sentiment Analysis:** Identifies the sentiment of the feedback (positive, negative, neutral).
- **Key Insights:** Extracts critical issues and themes mentioned in the feedback.
- **Actionable Recommendations:** Provides suggestions for improvement based on the analyzed feedback.
- **Web Interface:** A simple Gradio interface to input feedback and view the AI-generated insights.

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
python feedback_analyzer.py
```
The Gradio interface will open in your browser. You can now enter customer feedback to receive insights.

## File Descriptions

### `app.py`
The FastAPI backend application that exposes a POST endpoint `/analyze_feedback/` for analyzing customer feedback. It sends the feedback to the DeepSeek model and returns sentiment and insights.

#### Key Components:
- FastAPI for handling API requests.
- Uses the `requests` library to communicate with the DeepSeek AI model.

### `feedback_analyzer.py`
A script that creates a Gradio-based web interface for interacting with the AI model. Users can paste customer feedback, and the application will provide sentiment analysis, key issues, and recommended actions.

#### Key Components:
- Uses the `requests` library to interact with the DeepSeek API.
- Gradio is used for creating the user interface.

## Usage

1. **API Usage (FastAPI):**
   - POST your feedback to `http://127.0.0.1:8000/analyze_feedback/`.
   - Example payload:
     ```json
     {
       "feedback": "The product is great, but the delivery was late."
     }
     ```
   - The response will contain the sentiment and insights based on the feedback.

2. **Web Interface (Gradio):**
   - Enter customer feedback into the Gradio interface.
   - The app will display the sentiment, key themes, and actionable insights provided by the AI model.

## Example

### Sample Feedback:
"I love the laptop's performance, but the keyboard feels cheap."

### AI-Generated Insights:
- **Sentiment:** Neutral
- **Key Issues:** Keyboard quality
- **Suggested Action:** Improve keyboard design

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
