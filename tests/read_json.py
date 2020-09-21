import json

with open("tests/test_data.json", "r") as json_file:
    data = json.load(json_file)

print(data, type(data))
