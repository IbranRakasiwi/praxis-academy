import json
file_json = open("01-05/data_datar.json")

data = json.loads(file_json.read())

print(data)
