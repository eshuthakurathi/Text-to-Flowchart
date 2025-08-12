# Text-to-Flowchart Generator

A self-hosted chat application system that uses:
- Ollama (Mistral model) for generating Mermaid code from text.
- Kroki + Mermaid for rendering flowchart images.

## Folder Structure

app/
├── mistral.py # Interacts with Ollama
├── flowchart-generator.py # Sends Mermaid to Kroki
Docker/
└── docker-compose.yml # Starts Kroki + Mermaid
static/images/ # Stores generated flowchart images
main.py # Runs Flask API or UI

## Setup

1. Clone repo
2. Create virtual environment
3. Install dependencies
4. Run Docker services
5. Start the chatbot
