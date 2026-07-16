import json
import os

FILE_NAME = "memory.json"

def load_memory():

    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_memory(messages):

    with open(FILE_NAME, "w") as f:
        json.dump(messages, f, indent=4)