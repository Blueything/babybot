import requests
import os

API_KEY = "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"

def simulate_llm_response(prompt: str) -> dict:
    print("⚙️ Sending prompt to OpenRouter:", prompt)

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-4o-mini",
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            },
            timeout=15
        )

        res_json = response.json()
        print("🔍 Raw response:", res_json)

        if "choices" not in res_json:
            return {
                "message": "❌ Invalid response from LLM.",
                "tips": [res_json.get("error", {}).get("message", "No choices in response.")]
            }

        message = res_json["choices"][0]["message"]["content"].strip()
        lines = message.split("\n")
        main_message = lines[0].strip()

        def clean_text(line):
            return line.strip("-• ").strip().strip("*")

        tips = [clean_text(line) for line in lines[1:] if line.strip()]

        return {
            "message": clean_text(main_message),
            "tips": tips
        }

    except Exception as e:
        print("❌ OpenRouter Error:", e)
        return {
            "message": "⚠️ LLM unavailable.",
            "tips": ["Check your API key and network connection."]
        }
