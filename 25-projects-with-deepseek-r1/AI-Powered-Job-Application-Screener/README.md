
# AI-Powered Job Application Screener

## Overview
The **AI-Powered Job Application Screener** is a Python-based application that uses the DeepSeek AI model to analyze resumes and compare them with job descriptions. The project includes two main components: an API service built with FastAPI and a user-friendly web interface using Gradio. The application evaluates candidates' resumes, calculates a suitability score, and highlights matches or missing criteria based on the job description.

## Features
- **Resume Analysis:** Analyzes the content of resumes and compares them with the provided job description.
- **Suitability Score:** Provides a score (0-100%) based on the candidate’s skills and experience in relation to the job description.
- **Matches & Gaps:** Highlights matching skills and experience, as well as missing qualifications.
- **Web Interface:** A simple Gradio interface where users can paste a job description and resume content for evaluation.

## Requirements
- Python 3.7 or higher
- FastAPI
- Uvicorn (for running the FastAPI app)
- Gradio
- Requests
- PyMuPDF (for PDF resume text extraction)
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
python job_screener.py
```
The Gradio interface will open in your browser. You can now paste a resume and job description to evaluate candidate suitability.

## File Descriptions

### `app.py`
The FastAPI backend application that exposes a POST endpoint `/screen_candidate/` for screening resumes. It compares the provided resume with the job description and returns the suitability score and analysis.

#### Key Components:
- FastAPI for handling API requests.
- Uses the `requests` library to communicate with the DeepSeek AI model.

### `job_screener.py`
A script that creates a Gradio-based web interface for interacting with the AI model. Users can paste the resume text and job description, and the application will return the AI-generated suitability score and analysis of the candidate’s qualifications.

#### Key Components:
- Uses the `requests` library to interact with the DeepSeek API.
- Gradio is used for creating the user interface.
- PyMuPDF is used for extracting text from PDF resumes.

## Usage

1. **API Usage (FastAPI):**
   - POST your resume and job description to `http://127.0.0.1:8000/screen_candidate/`.
   - Example payload:
     ```json
     {
       "resume": "Name: John Doe, Experience: 1 year in Web Development, Skills: Java, Education: B.Sc. in Mechanical Engineering",
       "job_description": "Role: Backend Engineer, Required Skills: Python, Flask, SQL, API Development, Experience: 3+ years"
     }
     ```
   - The response will contain the AI-generated suitability score and analysis.

2. **Web Interface (Gradio):**
   - Paste the candidate’s resume and job description into the Gradio interface.
   - The app will display the AI-generated suitability score, highlighting matches and gaps in the qualifications.

## Example

### Sample Resume:
"Name: John Doe, Experience: 1 year in Web Development, Skills: Java, Education: B.Sc. in Mechanical Engineering"

### Sample Job Description:
"Role: Backend Engineer, Required Skills: Python, Flask, SQL, API Development, Experience: 3+ years"

### AI Screening Report:
- **Suitability Score:** 45%
- **Matches:** Experience in Web Development, Java skills.
- **Missing:** Python, Flask, SQL, 3+ years of experience.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
