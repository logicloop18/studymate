import json
import os

FILE = "data/data.json"


def load_data():
    if not os.path.exists(FILE):
        return {"tasks": [], "study_hours": 0}

    with open(FILE, "r") as file:
        return json.load(file)


def save_data(data):
    os.makedirs("data", exist_ok=True)

    with open(FILE, "w") as file:
        json.dump(data, file, indent=4)