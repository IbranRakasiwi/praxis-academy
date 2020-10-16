import json

# fail crd json
file_json = open("01-03/crc.json")

#panggil data json
data = json.loads(file_json.read())

# tampilkan
print (data)