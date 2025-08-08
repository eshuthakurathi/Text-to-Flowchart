import requests

def ensure_mermaid_starts_correctly(mermaid_code: str) -> str:
  """
  Ensures that the Mermaid code starts with a diagram type like 'graph TD'.
  Adds 'graph TD' if not already present.
  """
  mermaid_code = mermaid_code.strip()
  if not mermaid_code.startswith(("graph", "sequenceDiagram", "classDiagram", "stateDiagram", "erDiagram", "gantt", "pie", "journey")):
    mermaid_code = "graph TD\n" + mermaid_code
  return mermaid_code

def generate_flowchart(mermaid_code: str, output_path: str):
  """
  Sends Mermaid code to the Kroki server and saves the returned PNG image.
  """
  kroki_url = "http://localhost:8000"
  endpoint = f"{kroki_url}/mermaid/png"

  # Ensure Mermaid code is valid
  mermaid_code = ensure_mermaid_starts_correctly(mermaid_code)

  try:
    response = requests.post(endpoint, data=mermaid_code.encode("utf-8"))
    
    if response.ok:
      with open(output_path, "wb") as f:
        f.write(response.content)
      print(f"✅ Flowchart saved at: {output_path}")
    else:
      print("❌ Failed to generate flowchart.")
      print(f"❌ HTTP {response.status_code}: {response.reason}")
      print("❌ Response content:", response.text)

  except requests.exceptions.RequestException as e:
    print(f"❌ Request failed: {e}")
