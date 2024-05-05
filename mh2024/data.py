import json

def load_file(file):
    with open(f"./data/{file}.json", "r") as f:
        return json.load(f)

def post_file(data, file):
    with open(f"./data/{file}.json", "w") as f:
        json.dump(data, f, indent=4)