import os
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("HF_API_TOKEN")
if not token:
    print("Missing Hugging Face token!")
    exit()

headers = {"Authorization": f"Bearer {token}"}
api_url = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"

print("Chatbot ready! Type 'exit' to quit.\n")

while True:
    user_input = input("👤: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    payload = {"inputs": user_input}
    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 200:
        output = response.json()
        if isinstance(output, list) and "generated_text" in output[0]:
            print("🤖:", output[0]["generated_text"].strip())
        else:
            print("🤖:", output)
    else:
        print("Error:", response.text)
