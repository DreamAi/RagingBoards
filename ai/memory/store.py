# ai/memory/store.py
import json

def store_event(event):
    with open("data/memory.json", "a") as f:
        f.write(json.dumps(event) + "\n")
