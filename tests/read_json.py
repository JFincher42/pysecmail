import json

with open("tests/test_data.json", "r") as json_file:
    data = json.load(json_file)

for email in data:
    for field, value in enumerate(email):
        print(f"{value}: {email[value]}")
    print()