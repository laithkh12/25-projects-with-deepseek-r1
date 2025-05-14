
# AI-Powered Resume Generator

## Overview
The **AI-Powered Resume Generator** is a Python-based application that uses the DeepSeek AI model to automatically generate professional resumes. Users can input personal details such as name, job role, experience, skills, education, and a brief summary, and the AI will create a well-structured resume. The project includes two main components: an API service built with FastAPI and a web interface using Gradio. The application also generates a downloadable PDF of the resume.

## Features
- **Resume Generation:** Automatically generates a professional resume based on user input.
- **ATS-Friendly:** Ensures the resume is well-formatted and optimized for Applicant Tracking Systems (ATS).
- **PDF Generation:** Generates a downloadable PDF version of the resume.
- **Web Interface:** A simple Gradio interface for easy resume generation.

## Requirements
- Python 3.7 or higher
- FastAPI
- Uvicorn (for running the FastAPI app)
- Gradio
- Requests
- FPDF (for generating PDFs)
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
python resume_generator.py
```
The Gradio interface will open in your browser. You can now enter your details to generate a professional resume.

## File Descriptions

### `app.py`
The FastAPI backend application that exposes a POST endpoint `/resume/` for generating resumes based on user input. It sends the resume data to the DeepSeek AI model and returns the generated resume.

#### Key Components:
- FastAPI for handling API requests.
- Uses the `requests` library to communicate with the DeepSeek AI model.

### `resume_generator.py`
A script that creates a Gradio-based web interface for interacting with the AI model. Users can input their details, and the application will generate a professional resume in text format. The app also generates a downloadable PDF version of the resume.

#### Key Components:
- Uses the `requests` library to interact with the DeepSeek API.
- Gradio is used for creating the user interface.
- FPDF is used to generate PDF resumes.

## Usage

1. **API Usage (FastAPI):**
   - POST your details (name, job role, experience, skills, education, and summary) to `http://127.0.0.1:8000/resume/`.
   - Example payload:
     ```json
     {
       "name": "John Doe",
       "job_role": "Software Engineer",
       "experience": "3",
       "skills": "Python, AI, Web Development",
       "education": "B.Sc. CS",
       "summary": "Experienced in AI and cloud computing."
     }
     ```
   - The response will contain the AI-generated resume.

2. **Web Interface (Gradio):**
   - Enter your details in the Gradio interface.
   - The app will display the generated resume and provide a downloadable PDF option.

## Example

### Sample Resume Input:
- **Name:** John Doe
- **Job Role:** Software Engineer
- **Experience:** 3 years
- **Skills:** Python, AI, Web Development
- **Education:** B.Sc. CS
- **Summary:** Experienced in AI and cloud computing.

### AI-Generated Resume:
The AI will generate a resume that includes:
- Contact Information
- Objective
- Skills
- Experience
- Education
- Summary

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
