#contoh append
air = ["air hujan","air terjun"]
air.append("air mineral")
print (air)

#cara menggunakan list
minuman_bersoda = ["coca cola","c 100","suprite"]
print (minuman_bersoda)

# contoh menghapus 3
menghapus = ["rujak","gado gado","nasi pecel","nasi rawon"]
del menghapus [3]
print (menghapus)


# Kita punya list nama-nama buah
buah = ["apel", "anggur", "mangga", "jeruk"]

# Misanya kita ingin mengambil mangga
# Maka indeknya adalah 2
print buah[2]


buah = ["jeruk nipis", "apel", "mangga", "anggur"]
print (buah[2])
ouputnya 

"mangga"
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





