 # Struktur Data

    Hari kedua

Struktur data pada dasarnya hanya itu - mereka adalah struktur yang dapat menampung beberapa data bersama-sama. Dengan kata lain, mereka digunakan untuk menyimpan kumpulan data terkait.

Ada empat struktur data bawaan di Python - list, tuple, dictionary, dan set . Kita akan melihat bagaimana menggunakannya masing-masing dan bagaimana mereka membuat hidup kita lebih mudah.

Tutorial Struktur Data Python
Kenali struktur data Python: pelajari lebih lanjut tentang tipe data dan struktur data primitif serta non-primitif, seperti string, daftar, tumpukan, dll.

### Python
Python adalah bahasa pemrograman tujuan umum yang ditafsirkan, tingkat tinggi. Dibuat oleh Guido van Rossum dan pertama kali dirilis pada tahun 1991, filosofi desain Python menekankan keterbacaan kode dengan penggunaan spasi putih yang signifikan.

### List di Python
List adalah struktur data pada python yang mampu menyimpan lebih dari satu data, seperti array.

Pada kesempatan ini, kita akan membahas cara menggunakan list di Python dari yang paling sederhana sampai yang sedikit kompleks.
Apa saja poin-poin yang akan dipelajari?

    • Cara Membuat List dan Mengisinya
    • Cara Mangambil nilai dari List
    • Cara Menambahkan dan Menghapus isi List
    • Operasi pada List
    • List multi dimensi

Cara membuat lis di Python
List dapat kita buat seperti membuat variabel biasa, namun nilai variabelnya diisi dengan tanda kurung siku:

    buah = ["jeruk nipis", "apel", "mangga", "anggur"]
    print buah[2]

ouputnya 

    "mangga"


    #cara menggunakan list
    minuman_bersoda = ["coca cola","c 100","suprite"]
    print (minuman_bersoda)

Perintah di Atas Untuk mengisi.

    buah = ["jeruk", "apel", "mangga", "duren"]
    buah[2] = "kelapa"

ouputnya mengganti yang nomer dua seprti yang tertera diatas mangga akan terganti oleh kelapa 

    buah ["jeruk", "apel", "kelapa", "duren"]
    buah = ["jeruk", "apel", "mangga", "duren"]
    buah = ["jeruk", "apel", "mangga", "duren"]
    buah.append("manggis")

ouputnya akan menambahkan dari belakang.

    ["jeruk", "apel", "mangga", "duren", "manggis"]

    buah = ["jeruk", "apel", "mangga", "duren"]
    buah.prepend("anggur")

ouputnya akan menambahkan dari awalnya.

    ["anggur","jeruk", "apel", "mangga", "duren"]

        todo_list = [
            "Balajar Python",
            "Belajar Django",
            "Belajar MongoDB",
            "Belajar Sulap",
            "Belajar Flask"
        ]
        del todo_list[3]

        print todo_list

ouputnya akan mengapus yang ketiga.

    ['Balajar Python', 'Belajar Django', 'Belajar MongoDB', 'Belajar Flask']

    warna = ["merah", "hijau", "kuning", "biru", "pink", "ungu"]
    print warna[1:5]

ouputnya nomer saru dan lima

    ['hijau', 'kuning', 'biru', 'pink']

### contoh menghapus 2
    menghapus = ["rujak","gado gado","nasi pecel","nasi rawon"]
    del menghapus [3]
    print (menghapus)


contohnya

    minuman_bersoda = ["coca cola","c 100","suprite"]
    print (minuman_bersoda)


akan tampil 

    ['coca cola', 'c 100', 'suprite']

### contoh append (menambahkan) 
    air = ["air hujan","air terjun"]
    air.append("air mineral")
    print (air)

akan tampil 

    ['air hujan', 'air terjun', 'air mineral']



### contoh menghapus 
    menghapus = ["rujak","gado gado","nasi pecel","nasi rawon"]
    del menghapus [3]
    print (menghapus)

akan tampil 

    ['rujak', 'gado gado', 'nasi pecel']

### Operasi pada List 

    buah = ["apel", "anggur", "mangga", "jeruk"]
    print (buah[2])

akan tampil 

    mangga


## Modul

Modul
Modul adalah sebuah file yang berisi kode pemrograman python. Sebuah file yang berisi kode python, misalnya: example.py, disebut modul dan nama modulnya adalah example.

### Contoh modul di python

    def jumlah(a, b):
        """Fungsi ini menambahkan dua bilangan dan 
        mengembalikan hasilnya"""
    result = a + b
    return result

### Cara Mengambil Input dari Keyboard
Python sudah menyediakan fungsi input() dan raw_input() untuk mengambil inputan dari keyboard.

sebuah contoh…

### Mengambil input

    nama = raw_input("Siapa nama kamu: gibran")
    umur = input("Berapa umur kamu: 23")

### Menampilkan output
    print "Hello",gibran,"umur kamu adalah",23,"tahun"
    Hasilnya:

hasilanya

    "siapa nama kamu : gibran"

    "Berapa umur kamu : 23"

    "hallo gibran umur kamu adalah 23 tahun"

### untuk perulangan 

    # file: perulanganFor.py

    ulang = 15

    for i in range(ulang):
        print ("Perulangan ke-"+str(i))

hasilnya 

    /bin/python3.8 /home/tatam/Documents/praxis-academy/novice/01-03/hello.py
    Perulangan ke-0
    Perulangan ke-1
    Perulangan ke-2
    Perulangan ke-3
    Perulangan ke-4
    Perulangan ke-5
    Perulangan ke-6
    Perulangan ke-7
    Perulangan ke-8
    Perulangan ke-9
    Perulangan ke-10
    Perulangan ke-11
    Perulangan ke-12
    Perulangan ke-13
    Perulangan ke-14
    Perulangan ke-15


### list  untuk memotong dengan perintah 

    buah = ["kecut", "manis", "asem", "tawar", "tidak ada rasa"]

    print (buah [0:3])       #perintah potong list

hasilnya 

    ['kecut', 'manis', 'asem']

### List multi dimensi 

    list_makanan = [
        ["nasi","gado gado","rujak"],
        ["soto","bakso","lemper"],
        ["bubur ayam","gudeg","nasi goreng"]
    ]

    print (list_makanan[1][2])      #perintah 1 mengambil colom dan 2 mengambil baris
    for menu in list_makanan:       #perintah perulangan 
        for makanan in menu:
            print (makanan)

hasilnya

    lemper
    nasi
    gado gado
    rujak
    soto
    bakso
    lemper
    bubur ayam
    gudeg
    nasi goreng





















