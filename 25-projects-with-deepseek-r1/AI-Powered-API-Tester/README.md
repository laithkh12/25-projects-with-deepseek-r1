
# AI-Powered API Tester

## Overview
The **AI-Powered API Tester** is a Python-based application that leverages the DeepSeek AI model to validate API responses. It allows users to test API endpoints, check the status code, response time, and validate the presence of expected fields in the response. The project includes two main components: an API service built with FastAPI and a user-friendly web interface using Gradio. The application validates the response based on the expected fields and provides feedback.

## Features
- **API Testing:** Test API endpoints (GET and POST methods) for status code, response time, and payload validation.
- **AI-Based Validation:** Uses AI to check if the response contains the required fields and provide feedback.
- **Web Interface:** A simple Gradio interface where users can input API details and get the test results and validation feedback.

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

### 3. Launch the Gradio web interface:
```bash
python api_tester.py
```
The Gradio interface will open in your browser. You can now test API endpoints and validate their responses.

## File Descriptions

### `api_tester.py`
A script that creates a Gradio-based web interface for testing API responses. Users can input an API URL, specify the method (GET or POST), add headers, provide a payload, and define expected fields. The app sends the API request and provides test results, including validation feedback from the AI model.

#### Key Components:
- Uses the `requests` library to send HTTP requests to the API.
- Gradio is used for creating the user interface.
- AI validation is performed using the DeepSeek API to check for expected fields in the response.

## Usage

1. **Web Interface (Gradio):**
   - Enter the API URL and method (GET or POST).
   - Provide headers (optional), payload (optional), and expected fields (comma-separated).
   - The app will display the API test results, including the status code, response time, and AI validation feedback.

## Example

### Sample API Test:
- **API URL:** `https://jsonplaceholder.typicode.com/posts/1`
- **Method:** GET
- **Expected Fields:** userId, id, title, body

### AI-Generated Test Result:
- **Status Code:** 200
- **Response Time:** 50ms
- **Validation Feedback:** All expected fields are present: `userId`, `id`, `title`, `body`.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
