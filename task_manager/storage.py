import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as f:
        content = f.read().strip()

        # If file empty → return empty list
        if not content:
            return []

        try:
            return json.loads(content)
        except json.JSONDecodeError:
            return []  # If corrupted, reset automatically

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)
