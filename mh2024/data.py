import json

def add_user(user:str):
    cache:dict = load_file()
    cache[user] = {
        "Monday":{},
        "Tuesday":{},
        "Wednesday":{},
        "Thursday":{},
        "Friday":{},
        "Saturday":{},
        "Sunday":{}
    }
    post_file(cache)

def add_workout(user:str, day:str, workout:str, sets:list):
    cache:dict = load_file()
    if not user in cache: return
    cache[user][day][workout]=sets


def load_file():
    with open(f"./data/cache.json", "r") as f:
        return json.load(f)

def post_file(data):
    with open(f"./data/cache.json", "w") as f:
        json.dump(data, f, indent=4)