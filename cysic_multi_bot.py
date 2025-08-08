import requests
import json
import time

api_key = "YOUR_API_KEY_HERE"
base_url = "https://api-ai.cysic.xyz"

models = [
    "phi-4",
    "QwQ-32B-Q4_K_M",
    "Meta-Llama-3-8B-Instruc",
    "Llama-Guard-3-8B",
    "DeepSeek-R1-0528-Qwen3-8B",
    "gemma-2-9b-it"
]

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Load questions from file
with open("questions.txt", "r") as file:
    questions = [line.strip() for line in file if line.strip()]

def ask_cysic(model, question):
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant"},
            {"role": "user", "content": question}
        ]
    }
    try:
        response = requests.post(
            f"{base_url}/api/ai/chat/completions",
            headers=headers,
            data=json.dumps(payload)
        )
        response.raise_for_status()
        return
