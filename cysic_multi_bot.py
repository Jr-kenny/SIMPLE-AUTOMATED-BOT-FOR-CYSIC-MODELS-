import requests
import json
import time
import os

# Load API key from environment variable (safer)
api_key = os.getenv("CYSIC_API_KEY", "YOUR_API_KEY_HERE")
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
        data = response.json()

        # Extract text safely (depends on API structure)
        if "choices" in data and len(data["choices"]) > 0:
            return data["choices"][0]["message"]["content"]
        else:
            return "⚠️ No response from model."

    except requests.exceptions.RequestException as e:
        return f"❌ Error with {model}: {e}"

# Main loop
for question in questions:
    print(f"\n📝 Question: {question}\n")
    for model in models:
        print(f"🤖 Asking {model}...")
        answer = ask_cysic(model, question)
        print(f"👉 {model} reply: {answer}\n")
        time.sleep(2)  # pause to avoid spamming the API
