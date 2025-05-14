
# AI-Powered PDF Text Extractor

## Overview
The **AI-Powered PDF Text Extractor** is a Python-based application that allows users to extract text from PDF files. The project includes two main components: an API service built with FastAPI and a user-friendly web interface using Gradio. The app uses the PyMuPDF library to extract text from PDF files and supports OCR (Optical Character Recognition) for scanned PDFs using Tesseract. Additionally, the application can summarize the extracted text using the DeepSeek AI model.

## Features
- **PDF Text Extraction:** Extracts text from PDF documents using PyMuPDF.
- **OCR for Scanned PDFs:** Uses Tesseract OCR to extract text from scanned PDF images.
- **Text Summarization:** Summarizes the extracted text using the DeepSeek AI model.
- **Web Interface:** A simple Gradio interface to upload PDFs and extract or summarize the text.

## Requirements
- Python 3.7 or higher
- FastAPI
- Uvicorn (for running the FastAPI app)
- Gradio
- Requests
- PyMuPDF (for extracting text from PDFs)
- pytesseract and pdf2image (for OCR-based text extraction)
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
python pdf_text_extractor.py
```
The Gradio interface will open in your browser. You can now upload a PDF to extract or summarize its text.

## File Descriptions

### `app.py`
The FastAPI backend application that exposes a POST endpoint `/extract_text/` for extracting text from a PDF file. It uses PyMuPDF to extract text from PDF documents and returns the extracted text.

#### Key Components:
- FastAPI for handling API requests.
- Uses the `requests` library to communicate with the DeepSeek AI model.

### `pdf_text_extractor.py`
A script that creates a Gradio-based web interface for interacting with the AI model. Users can upload PDF files, extract text, or use OCR for scanned documents. The app also summarizes the extracted text.

#### Key Components:
- Uses the `requests` library to interact with the DeepSeek API for text summarization.
- Gradio is used for creating the user interface.
- PyMuPDF for extracting text from regular PDFs.
- pytesseract and pdf2image for extracting text from scanned PDF files using OCR.

## Usage

1. **API Usage (FastAPI):**
   - POST a PDF file to `http://127.0.0.1:8000/extract_text/` for text extraction.
   - Example payload (upload file):
     ```json
     {
       "file": "<PDF file>"
     }
     ```
   - The response will contain the extracted text from the PDF.

2. **Web Interface (Gradio):**
   - Upload a PDF file in the Gradio interface.
   - The app will extract the text or apply OCR if the PDF is scanned.
   - The app also supports summarizing the extracted text.

## Example

### Sample PDF Text Extraction:
- **Uploaded PDF:** A research paper on climate change.
- **Extracted Text:** The document discusses the effects of climate change on ocean currents, temperature shifts, and extreme weather patterns.

### AI-Generated Summary:
"Climate change significantly impacts ocean currents and weather patterns. Increased temperatures contribute to more frequent and severe storms."

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
