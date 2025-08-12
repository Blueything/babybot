import requests

def simulate_llm_response(prompt: str) -> dict:
    print("⚙️ Sending prompt to LLM:", prompt)

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            },
            timeout=15  # 🕒 max wait time in seconds
        )
        data = response.json()["response"].strip()
        print("✅ LLM Response:", data)

        return {
            "message": data,
            "tips": [line.strip("-• ") for line in data.split("\n") if line.strip()]
        }

    except Exception as e:
        print("❌ LLM Error:", e)
        return {
            "message": "⚠️ LLM unavailable.",
            "tips": ["Make sure Ollama is running."]
        }
