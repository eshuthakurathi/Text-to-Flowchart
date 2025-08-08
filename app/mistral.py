import requests

# URL of your local Ollama server
OLLAMA_URL = "http://localhost:11434/api/generate"

# System prompt that instructs the model to only return valid Mermaid flowcharts
SYSTEM_PROMPT = """
You are a Mermaid flowchart generator. 
Only return a valid mermaid diagram that fits the prompt. Do not include explanations or markdown formatting.
Start your response with "graph TD".
"""

def generate_response(prompt: str) -> str:
  payload = {
    "model": "mistral", 
    "prompt": f"{SYSTEM_PROMPT.strip()}\n\n{prompt}",
    "stream": False
  }

  try:
    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()
    data = response.json()

    return data.get("response", "").strip()

  except requests.exceptions.RequestException as e:
    print(f"❌ Error communicating with Ollama: {e}")
    return "graph TD\nError --> Could not generate flowchart"
