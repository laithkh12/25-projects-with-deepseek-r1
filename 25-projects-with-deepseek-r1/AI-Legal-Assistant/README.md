
# AI-Legal Assistant

## Overview
The **AI-Legal Assistant** is a Python-based application that uses the DeepSeek AI model to generate professional legal documents. It helps users create various types of legal documents, including rental agreements, employment contracts, business partnership agreements, and non-disclosure agreements (NDAs). The project consists of two main components: an API service built with FastAPI and a user-friendly web interface using Gradio. This AI-powered assistant can quickly generate legally sound contracts based on user input.

## Features
- **Document Generation:** Automatically generates legal documents such as rental agreements, employment contracts, business partnership agreements, and NDAs.
- **Template-Based:** The AI uses pre-defined templates to ensure legal correctness and consistency in the documents.
- **Web Interface:** A simple Gradio interface where users can choose the document type, enter party names, and get a professional legal contract.

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
python legal_assistant.py
```
The Gradio interface will open in your browser. You can now select the document type and enter the details to generate the legal document.

## File Descriptions

### `app.py`
The FastAPI backend application that exposes a POST endpoint `/legal/` for generating legal documents. It sends the provided text to the DeepSeek AI model and returns the generated document.

#### Key Components:
- FastAPI for handling API requests.
- Uses the `requests` library to communicate with the DeepSeek AI model.

### `legal_assistant.py`
A script that creates a Gradio-based web interface for interacting with the AI model. Users can select the document type, provide party names, and input additional details (e.g., duration, salary) to generate the legal document.

#### Key Components:
- Uses the `requests` library to interact with the DeepSeek API.
- Gradio is used for creating the user interface.
- Generates documents for rental agreements, employment contracts, business partnership agreements, and NDAs.

## Usage

1. **API Usage (FastAPI):**
   - POST your input to `http://127.0.0.1:8000/legal/`.
   - Example payload:
     ```json
     {
       "text": "Generate a rental agreement between John Doe (tenant) and Jane Smith (landlord) for 12 months."
     }
     ```
   - The response will contain the AI-generated legal document.

2. **Web Interface (Gradio):**
   - Select the document type.
   - Enter the required information (e.g., party names, duration, salary).
   - The app will display the AI-generated legal document.

## Example

### Sample Request:
- **Document Type:** Rental Agreement
- **Party 1 Name:** John Doe
- **Party 2 Name:** Jane Smith
- **Duration:** 12 months
- **Salary:** (not applicable)

### AI-Generated Document:
- **Rental Agreement** between John Doe (tenant) and Jane Smith (landlord) for a duration of 12 months.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
