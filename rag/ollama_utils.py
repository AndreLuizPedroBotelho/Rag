import json
import requests

OLLAMA_URL = "http://localhost:11434"
MODEL = "mistral"

def ollama_stream(prompt: str):
    payload = {"model": MODEL, "prompt": prompt, "stream": True}
    with requests.post(f"{OLLAMA_URL}/api/generate", json=payload, stream=True) as r:
        for line in r.iter_lines():
            if line:
                try:
                    data = json.loads(line)
                    yield data.get("response", "")
                except json.JSONDecodeError:
                    continue
