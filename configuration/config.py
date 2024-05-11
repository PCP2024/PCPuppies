import json

hard_coded_values = {
    "threshold": {
        "threshold": "20",
    }, 
    "rotate": {
        "degree": "35",
    }
}

with open(".\configuration\config.json", "w") as write_file:
    json.dump(hard_coded_values, write_file)

with open(".\configuration\config.json", "r") as read_file:
    data = json.load(read_file)

print(data)