from app.mistral import generate_response
from app.flowchart_generator import generate_flowchart
import os
import uuid

def main():
  # Ask for user prompt in terminal
  prompt = input("📥 Enter your flowchart description: ").strip()
  
  if not prompt:
    print("❌ No input provided.")
    return

  # Step 1: Generate mermaid code
  mermaid_code = generate_response(prompt)
  print("\n🧠 Mermaid code generated:\n")
  print(mermaid_code)

  # Step 2: Create output directory if not exists
  output_dir = os.path.join("static", "images")
  os.makedirs(output_dir, exist_ok=True) 

  # Step 3: Save the flowchart image
  image_filename = f"{uuid.uuid4()}.png"
  image_path = os.path.join(output_dir, image_filename)
  generate_flowchart(mermaid_code, image_path)


if __name__ == "__main__":
  main()
