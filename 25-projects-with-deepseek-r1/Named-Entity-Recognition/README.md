
# AI-Powered Named Entity Recognition (NER)

## Overview
The **AI-Powered Named Entity Recognition (NER)** is a Python-based application that uses the DeepSeek AI model to extract named entities such as persons, organizations, locations, and dates from a given text. The project includes two main components: an API service built with FastAPI and a user-friendly web interface using Gradio. This tool can be used to extract important information from unstructured text data.

## Features
- **Named Entity Extraction:** Automatically extracts named entities such as persons, organizations, locations, and dates from text.
- **Text Input:** Users can input text, and the AI will extract the relevant entities.
- **Web Interface:** A simple Gradio interface to enter text and get AI-generated entity extraction.

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
python ner_extractor.py
```
The Gradio interface will open in your browser. You can now enter text, and the app will provide the extracted named entities.

## File Descriptions

### `app.py`
The FastAPI backend application that exposes a POST endpoint `/extract_entities` for named entity recognition. It sends the provided text to the DeepSeek AI model and returns the extracted entities.

#### Key Components:
- FastAPI for handling API requests.
- Uses the `requests` library to communicate with the DeepSeek AI model.

### `ner_extractor.py`
A script that creates a Gradio-based web interface for interacting with the AI-powered NER model. Users can input text, and the application will return the extracted named entities such as persons, organizations, locations, and dates.

#### Key Components:
- Uses the `requests` library to interact with the DeepSeek API.
- Gradio is used for creating the user interface.

## Usage

1. **API Usage (FastAPI):**
   - POST your text to `http://127.0.0.1:8000/extract_entities`.
   - Example payload:
     ```json
     {
       "text": "Google was founded by Larry Page and Sergey Brin in September 1998 at Stanford University."
     }
     ```
   - The response will contain the AI-generated extracted entities.

2. **Web Interface (Gradio):**
   - Enter your text into the Gradio interface.
   - The app will display the extracted named entities such as persons, organizations, locations, and dates.

## Example

### Sample Text:
"Google was founded by Larry Page and Sergey Brin in September 1998 at Stanford University."

### AI-Extracted Entities:
- **Persons:** Larry Page, Sergey Brin
- **Organizations:** Google, Stanford University
- **Dates:** September 1998
- **Locations:** Stanford University

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
