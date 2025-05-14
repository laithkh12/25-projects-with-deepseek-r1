
# AI-Powered E-commerce Product Recommendation Bot

## Overview
The **AI-Powered E-commerce Product Recommendation Bot** is a Python-based application that uses the DeepSeek AI model to recommend products based on customer queries. The project includes two main components: an API service built with FastAPI and a user-friendly web interface using Gradio. The bot analyzes customer queries and provides product recommendations from a pre-defined product database, including categories like laptops, smartphones, and headphones.

## Features
- **Product Recommendations:** Provides product recommendations based on the user's query.
- **Product Categories:** Supports multiple product categories, such as laptops, smartphones, and headphones.
- **Web Interface:** A simple Gradio interface that allows users to enter their product queries and get AI-generated recommendations.

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
python product_recommender.py
```
The Gradio interface will open in your browser. You can now enter your product query and get AI-generated recommendations.

## File Descriptions

### `app.py`
The FastAPI backend application that exposes a POST endpoint `/recommend/` for generating product recommendations. It sends the user's query to the DeepSeek AI model and returns the AI-generated product recommendations.

#### Key Components:
- FastAPI for handling API requests.
- Uses the `requests` library to communicate with the DeepSeek AI model.

### `product_recommender.py`
A script that creates a Gradio-based web interface for interacting with the AI-powered product recommendation bot. Users can enter a product query, and the application will return AI-generated product recommendations based on the query.

#### Key Components:
- Uses the `requests` library to interact with the DeepSeek API.
- Gradio is used for creating the user interface.
- A predefined product database is used for generating recommendations.

## Usage

1. **API Usage (FastAPI):**
   - POST your query to `http://127.0.0.1:8000/recommend/`.
   - Example payload:
     ```json
     {
       "query": "best smartphone under $500"
     }
     ```
   - The response will contain the AI-generated product recommendations.

2. **Web Interface (Gradio):**
   - Enter your product query into the Gradio interface.
   - The app will display the AI-generated product recommendations.

## Example

### Sample Query:
"Best laptop for gaming under $1000"

### AI-Generated Recommendations:
- **Apple MacBook Air M2 – Lightweight, powerful, and great battery life.**
- **Dell XPS 13 – High performance with a sleek design.**
- **Lenovo ThinkPad X1 Carbon – Ideal for business professionals.**

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
