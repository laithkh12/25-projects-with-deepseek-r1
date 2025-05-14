
# AI-Powered Email Responder

## Overview
The **AI-Powered Email Responder** is a Python-based application that uses the DeepSeek AI model to automatically generate email responses based on the provided email content. Users can specify the tone of the response, such as Formal, Casual, or Friendly. The project includes two main components: an API service built with FastAPI and a user-friendly web interface using Gradio. The application can generate professional, polite, and clear email responses for customer support, business correspondence, or personal communication.

## Features
- **Email Response Generation:** Automatically generates an email response based on the provided email content.
- **Customizable Tone:** Choose between Formal, Casual, or Friendly tones for the email response.
- **Web Interface:** A simple Gradio interface that allows users to input email content and select the tone for the response.

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
python email_responder.py
```
The Gradio interface will open in your browser. You can now input an email and select the tone to generate a response.

## File Descriptions

### `app.py`
The FastAPI backend application that exposes a POST endpoint `/email/` for generating email responses. It sends the email content and tone to the DeepSeek AI model and returns the AI-generated email response.

#### Key Components:
- FastAPI for handling API requests.
- Uses the `requests` library to communicate with the DeepSeek AI model.

### `email_responder.py`
A script that creates a Gradio-based web interface for interacting with the AI model. Users can paste the email content and select the tone of the response (Formal, Casual, or Friendly).

#### Key Components:
- Uses the `requests` library to interact with the DeepSeek API.
- Gradio is used for creating the user interface.
- The app generates polite, clear, and professional email responses.

## Usage

1. **API Usage (FastAPI):**
   - POST the email content and tone to `http://127.0.0.1:8000/email/`.
   - Example payload:
     ```json
     {
       "email_content": "Dear Support, I need help with my recent purchase.",
       "tone": "Formal"
     }
     ```
   - The response will contain the AI-generated email response.

2. **Web Interface (Gradio):**
   - Paste the email content into the Gradio interface.
   - Select the desired tone (Formal, Casual, or Friendly).
   - The app will display the AI-generated email response.

## Example

### Sample Email Content:
"Dear Support, I need help with my recent purchase."

### AI-Generated Response (Formal):
"Dear Customer,  
Thank you for reaching out to us. We are happy to assist you with your recent purchase. Please provide more details, and we will address your concerns promptly.  
Best regards,  
Customer Support Team"

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
