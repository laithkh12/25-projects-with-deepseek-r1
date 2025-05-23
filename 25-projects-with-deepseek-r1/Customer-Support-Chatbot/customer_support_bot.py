import requests
import gradio as gr

OLLAMA_URL = "http://localhost:11434/api/generate"

FAQ_DB = {
    "order tracking": "You can track your order by logging into your account and navigating to 'My Orders'.",
    "return policy": "We accept returns within 30 days. Visit our Returns page to initiate a return.",
    "customer support contact": "You can reach customer support at support@example.com or call us at +1-800-555-1234.",
    "payment methods": "We accept Visa, MasterCard, PayPal, and Apple Pay for secure transactions.",
    "shipping details": "Orders are processed within 24 hours. Standard shipping takes 3-5 business days."
}

def chatbot_response(user_query, language="English"):
    prompt = f"Find the best match from the FAQ database for this customer query:\n\n'{user_query}'\n\n" \
             f"Available FAQs: {list(FAQ_DB.keys())}\n" \
             f"Provide a response based on the closet matching FAQ in {language}"
    
    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False,
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        ai_response = response.json().get("response", "I'm sorry, I don't have an answer for that.")
        return FAQ_DB.get(ai_response.lower(), ai_response)
    else:
        return "Sorry, I couldn't process your request."


interface = gr.Interface(
    fn=chatbot_response, 
    inputs=gr.Textbox(lines=2, placeholder="Ask your customer support a question..."),
    outputs=gr.Textbox(label="Chatbot Response"),
    title="AI-Powered Customer Support Chatbot",
    description="Ask a question, and the AI will respond with the best-matching FAQ answer."
)  


if __name__ == "__main__":
    interface.launch()

# if __name__ == "__main__":
#     sample_query = "How can I return a product?"
#     print("### Chatbot Answer ###")
#     print(chatbot_response(sample_query))