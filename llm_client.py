import os
import requests

ASI_ONE_URL = "https://api.asi1.ai/v1/chat/completions"
ASI_ONE_API_KEY = os.getenv("ASI_ONE_API_KEY")  # lee la key desde variable de entorno

def query_llm(prompt: str) -> str:
    if not ASI_ONE_API_KEY:
        raise ValueError("⚠️ No se encontró la API key. Define la variable de entorno ASI_ONE_API_KEY.")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ASI_ONE_API_KEY}"
    }
    data = {
        "model": "asi1-mini",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(ASI_ONE_URL, headers=headers, json=data)
    result = response.json()

    try:
        return result["choices"][0]["message"]["content"].strip()
    except Exception:
        return f"❌ Error en la respuesta del LLM: {result}"
