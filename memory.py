import json

data = {
    "users": {
        "id": 1,
        "name": "Abhiram",
        "branch": "Cybersecurity",
        "age": 18
    }
}

with open("memory.json", "w") as file:
    json.dump(data, file)