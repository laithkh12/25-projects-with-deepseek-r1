
# AI-Powered SQL Query Generator

## Overview
The **AI-Powered SQL Query Generator** is a Python-based application that uses the DeepSeek AI model to convert natural language queries into SQL queries. The project includes two main components: an API service built with FastAPI and a user-friendly web interface using Gradio. This tool is designed to help users generate SQL queries based on their natural language input, making it easier to work with databases.

## Features
- **Natural Language to SQL Conversion:** Converts natural language queries into SQL queries.
- **Supports Multiple Databases:** Can generate SQL queries for various databases like MySQL, PostgreSQL, and SQLite.
- **Web Interface:** A simple Gradio interface where users can input natural language queries and get AI-generated SQL queries.

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
python sql_query_generator.py
```
The Gradio interface will open in your browser. You can now input a natural language query, and the app will generate the corresponding SQL query.

## File Descriptions

### `app.py`
The FastAPI backend application that exposes a POST endpoint `/generate_sql/` for generating SQL queries. It sends the user's natural language query and optional database schema to the DeepSeek AI model and returns the generated SQL query.

#### Key Components:
- FastAPI for handling API requests.
- Uses the `requests` library to communicate with the DeepSeek AI model.

### `sql_query_generator.py`
A script that creates a Gradio-based web interface for interacting with the AI-powered SQL query generator. Users can input a natural language query and an optional database schema, and the application will return the corresponding SQL query.

#### Key Components:
- Uses the `requests` library to interact with the DeepSeek API.
- Gradio is used for creating the user interface.

## Usage

1. **API Usage (FastAPI):**
   - POST your natural language query to `http://127.0.0.1:8000/generate_sql/`.
   - Example payload:
     ```json
     {
       "natural_query": "List all employees in the Sales department.",
       "schema": "employee(name, salary, department)"
     }
     ```
   - The response will contain the AI-generated SQL query.

2. **Web Interface (Gradio):**
   - Enter your natural language query and database schema (optional) in the Gradio interface.
   - The app will display the AI-generated SQL query.

## Example

### Sample Query:
"List all employees in the Sales department."

### AI-Generated SQL Query:
```sql
SELECT * FROM employee WHERE department = 'Sales';
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
