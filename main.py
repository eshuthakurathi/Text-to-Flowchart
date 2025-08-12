from flask import Flask, request, jsonify, send_file
from app.mistral import generate_response
from app.flowchart_generator import generate_flowchart
import os
import uuid

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
  data = request.json
  prompt = data.get("prompt")

  if not prompt:
    return jsonify({"error": "No prompt provided"}), 400

  # Step 1: Generate mermaid code from text
  mermaid_code = generate_response(prompt)

  # Step 2: Generate image from mermaid code using Kroki
  image_filename = f"{uuid.uuid4()}.png"
  image_path = os.path.join("static", "images", image_filename)
  generate_flowchart(mermaid_code, image_path)

  return jsonify({"image_url": f"/image/{image_filename}"})


@app.route("/image/<filename>")
def serve_image(filename):
  return send_file(os.path.join("static", "images", filename), mimetype='image/png')


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)