
# AI-Powered Content Writer

## Overview
The **AI-Powered Content Writer** is a Python-based application that uses the DeepSeek AI model to generate content based on a specified topic, keywords, and tone. The project includes two main components: an API service built with FastAPI and a user-friendly web interface using Gradio. The application can generate blog posts, marketing content, and social media posts with customizable tones like Professional, Casual, or Persuasive.

## Features
- **Content Generation:** Automatically generates blog posts and marketing content based on the user's input.
- **Tone Customization:** Choose between Professional, Casual, or Persuasive tones for the generated content.
- **Social Media Post Generation:** Generates engaging posts for platforms like Twitter based on the topic.
- **Web Interface:** A simple Gradio interface that allows users to input topics, keywords, and tone to generate content.

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
python content_writer.py
```
The Gradio interface will open in your browser. You can now enter a topic, keywords, and tone to generate content.

## File Descriptions

### `app.py`
The FastAPI backend application that exposes a POST endpoint `/generate_content/` for content generation. It sends the user's input (topic, keywords, tone) to the DeepSeek AI model and returns the generated content.

#### Key Components:
- FastAPI for handling API requests.
- Uses the `requests` library to communicate with the DeepSeek AI model.

### `content_writer.py`
A script that creates a Gradio-based web interface for interacting with the AI model. Users can input a topic, select keywords, and choose the tone of the content to generate blog posts or marketing content.

#### Key Components:
- Uses the `requests` library to interact with the DeepSeek API.
- Gradio is used for creating the user interface.
- Supports generating blog posts, marketing content, and social media posts for various platforms.

## Usage

1. **API Usage (FastAPI):**
   - POST your topic, keywords, and tone to `http://127.0.0.1:8000/generate_content/`.
   - Example payload:
     ```json
     {
       "topic": "The Future of AI",
       "keywords": "AI, automation, deep learning",
       "tone": "Professional"
     }
     ```
   - The response will contain the AI-generated content (e.g., a blog post).

2. **Web Interface (Gradio):**
   - Enter your topic and keywords into the Gradio interface.
   - Select the desired tone (Professional, Casual, or Persuasive).
   - The app will display the AI-generated content (blog post, social media post, etc.).

## Example

### Sample Topic:
"The Future of AI"

### Sample Keywords:
"AI, automation, deep learning"

### AI-Generated Content (Professional Tone):
"The future of artificial intelligence (AI) promises a revolution in automation and deep learning. As AI technology continues to evolve, its applications in industries such as healthcare, finance, and education will become increasingly impactful. In this blog post, we will explore the potential of AI to transform industries, improve productivity, and enhance human capabilities."

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
