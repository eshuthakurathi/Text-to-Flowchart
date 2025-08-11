import requests

# URL of your local Ollama server
OLLAMA_URL = "http://localhost:11434/api/generate"

# System prompt that instructs the model to only return valid Mermaid flowcharts
SYSTEM_PROMPT = """
You are a Mermaid flowchart generator.
Only return valid Mermaid syntax.
Always use proper arrow notation: --> for normal arrows, --x for crosses.
Do not omit arrow heads.
Do not include any explanations or markdown.
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
