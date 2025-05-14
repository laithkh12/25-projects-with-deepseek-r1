
# AI-Powered Research Paper Summarizer

## Overview
The **AI-Powered Research Paper Summarizer** is a Python-based application that uses the DeepSeek AI model to summarize academic research papers. The project includes two main components: an API service built with FastAPI and a user-friendly web interface using Gradio. The application extracts key sections (such as abstract, methodology, results, and conclusion) from the provided research paper text and generates a concise summary with insights.

## Features
- **Research Paper Summarization:** Automatically summarizes academic research papers by extracting key sections.
- **AI-Generated Insights:** Provides a structured summary of the paper, including insights into the methodology, results, and conclusion.
- **Web Interface:** A simple Gradio interface to input or upload a research paper for summarization.

## Requirements
- Python 3.7 or higher
- FastAPI
- Uvicorn (for running the FastAPI app)
- Gradio
- Requests
- PyMuPDF (for extracting text from PDF)
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
python paper_summarizer.py
```
The Gradio interface will open in your browser. You can now upload a research paper or paste its content to generate a structured summary.

## File Descriptions

### `app.py`
The FastAPI backend application that exposes a POST endpoint `/summarize_paper/` for summarizing research papers. It sends the paper content to the DeepSeek AI model and returns the AI-generated summary.

#### Key Components:
- FastAPI for handling API requests.
- Uses the `requests` library to communicate with the DeepSeek AI model.

### `paper_summarizer.py`
A script that creates a Gradio-based web interface for interacting with the AI model. Users can paste the research paper content, and the application will return a structured summary, extracting key sections such as the abstract, methodology, results, and conclusion.

#### Key Components:
- Uses the `requests` library to interact with the DeepSeek API.
- Gradio is used for creating the user interface.
- PyMuPDF is used for extracting text from PDF research papers.

## Usage

1. **API Usage (FastAPI):**
   - POST the research paper content to `http://127.0.0.1:8000/summarize_paper/`.
   - Example payload:
     ```json
     {
       "paper_text": "This study examines how AI impacts climate change predictions using deep learning models..."
     }
     ```
   - The response will contain the AI-generated research summary.

2. **Web Interface (Gradio):**
   - Paste the research paper text into the Gradio interface.
   - The app will display the AI-generated structured summary with key sections.

## Example

### Sample Research Paper Text:
"This study examines how AI impacts climate change predictions using deep learning models, focusing on methodologies, datasets, and results."

### AI-Generated Research Summary:
- **Abstract:** The paper discusses the use of AI in predicting climate change.
- **Methodology:** Deep learning models are employed with various datasets.
- **Results:** The models demonstrate promising accuracy.
- **Conclusion:** AI can significantly improve climate predictions.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
