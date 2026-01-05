import requests
from app.config import GEMINI_API_KEY

def ask_gemini(prompt: str) -> str:
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        "gemini-pro:generateContent"
        f"?key={GEMINI_API_KEY}"
    )

    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

    return response.json()["candidates"][0]["content"]["parts"][0]["text"]
