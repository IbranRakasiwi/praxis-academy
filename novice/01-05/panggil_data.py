# gunakan modul json
import json

# buka file JSON
file_json = open("01-05/dataku.json")

# prsing data JSON
data = json.loads(file_json.read())

# cetak isi data JSON
print(data)