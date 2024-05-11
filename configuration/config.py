import json

hard_coded_values = {
    "variables": {
        "name": "PCP",
        "year": "2024"
    }
}

with open("config.json", "w") as write_file:
    json.dump(hard_coded_values, write_file)

with open("config.json", "r") as read_file:
    data = json.load(read_file)

print(data)