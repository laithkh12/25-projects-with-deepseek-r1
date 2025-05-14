import requests
import gradio as gr

OLLAMA_URL = "http://localhost:11434/api/generate"

PRODUCT_DB = {
    "laptop": [
        "Apple MacBook Air M2 – Lightweight, powerful, and great battery life.",
        "Dell XPS 13 – High performance with a sleek design.",
        "Lenovo ThinkPad X1 Carbon – Ideal for business professionals."
    ],
    "smartphone": [
        "iPhone 14 – Great camera and iOS experience.",
        "Samsung Galaxy S23 – High-performance Android flagship.",
        "Google Pixel 7 – Best AI-powered camera features."
    ],
    "headphones": [
        "Sony WH-1000XM4 – Industry-leading noise cancellation.",
        "Bose QuietComfort 45 – Superior comfort and sound quality.",
        "Anker Soundcore Life Q30 – Best budget ANC headphones."
    ]
}

def recommend_products(query):
    prompt = f"Analyze the following user query and recommend the best matching products:\n\nQuery: {query}\n\n" \
    f"Avaliable product categories: {list(PRODUCT_DB.keys())}\n" \
    f"Provide a list of top recommendations."

    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False,
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        ai_response = response.json().get("response", "No recommendations for that.")
        for category in PRODUCT_DB:
            if category in query.lower():
                return "\n".join(PRODUCT_DB[category])
        return ai_response
    else:
        return f"Error: {response.text}" 
    

interface = gr.Interface(
    fn=recommend_products,
    inputs=gr.Textbox(lines=2, placeholder="Ask for product recommendaions (e.g., best smartphone under $500)"),
    outputs=gr.Textbox(label="Recommended Products"),
    title="AI-Powered E-commerce Recommendation Bot",
    description="Enter your query and get AI generated product recommendations"
)

if __name__ == "__main__":
    interface.launch()