import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

SYSTEM_PROMPT = """
You are a senior software engineer.
- Write clean and optimized code
- Explain clearly
- Suggest improvements
- Handle edge cases
"""

chat_history = []

def generate_response(user_input):
    try:
        chat_history.append(f"User: {user_input}")
        prompt = SYSTEM_PROMPT + "\n" + "\n".join(chat_history)

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "codellama",
                "prompt": prompt,
                "stream": False
            }
        )

        response.raise_for_status()
        result = response.json()["response"]
        chat_history.append(f"AI: {result}")
        return result

    except Exception as e:
        return f"Error: {str(e)}"
