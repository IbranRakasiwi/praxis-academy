# file: perulanganFor.py

ulang = 5

for i in range(ulang):
    print ("Perulangan ke-"+str(i))

 

buah = ["kecut", "manis", "asem", "tawar", "tidak ada rasa"]

print (buah [0:3])       #perintah potong list


list_makanan = [
    ["nasi","gado gado","rujak"],
    ["soto","bakso","lemper"],
    ["bubur ayam","gudeg","nasi goreng"]
]

print (list_makanan[1][2])      #perintah 1 mengambil colom dan 2 mengambil baris
for menu in list_makanan:       #perintah perulangan 
    for makanan in menu:
        print (makanan)

pertanyaan = "gimana kabarmu?",      #ini tuple
jawaban = 'alhamdulillah'       #ini string

print (pertanyaan)
print (jawaban)

nomor = {11, 12, 13, 'angka',15}

print (nomor)

nomor = [11, 12, 13, 'angka',15]

print (nomor)