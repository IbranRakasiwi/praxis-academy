## Struktur data

    Hari kedua

Struktur data adalah struktur yang dapat menampung beberapa data bersama-sama. Dengan kata lain, mereka digunakan untuk menyimpan kumpulan data terkait.

Ada empat struktur data bawaan di Python - list, tuple, dictionary, dan set . Kita akan melihat bagaimana menggunakannya masing-masing dan bagaimana mereka membuat hidup kita lebih mudah.

Tutorial Struktur Data Python
Kenali struktur data Python: pelajari lebih lanjut tentang tipe data dan struktur data primitif serta non-primitif, seperti string, daftar, tumpukan, dll.

### Manfaat struktur data

Bayangkan sebuah skenario dimana kita memiliki kebutuhan untuk memproses data ribuan mahasiswa. Untuk setiap mahasiswa kita perlu menyimpan data nomor induk, nama, program studi, dan seterusnya. Untuk dapat melakukan pemrosesan, tentunya kita ingin menyimpan data-data tersebut ke dalam variabel. Mendeklarasikan variabel sejumlah mahasiswa yang ada tentu saja sangat tidak efisien, apalagi bila kemudian data tersebut bisa berubah ukurannya.

Untuk menangani kebutuhan seperti pada kasus di atas, kita memerlukan variabel yang dapat menampung koleksi data/banyak data sekaligus sekaligus memudahkan akses dan pengelolaannya. Pada kasus inilah struktur data muncul sebagai jawabannya.

Struktur data, secara lebih spesifik, dapat dimakanai sebagai kumpulan/koleksi data mencakup nilai, relasi , serta operasi yang dapat dilakukan terhadapnya. Dalam bahasa pemrograman python dikenal empat struktur data built in, yakni list, tuple, dictionary, dan set. Berdasarkan karakternya, struktur data dapat tergolong ordered atau unordered, mutable atau immutable.



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

    person1 = {
    "nama": "gibran",
    "tahun": 24,
    "negara": "indonesia"
    }

### Cara Mengambil Input dari Keyboard
Python sudah menyediakan fungsi input() dan raw_input() untuk mengambil inputan dari keyboard.

## Input dan Menampilkan Output

Input adalah masukan yang kita berikan ke program.Program akan memprosesnya dan menampilkan hasil outputnya. Input, proses, dan output adalah inti dari semua program komputer.

belajar cara mengambil input dan menampilkan output untuk program berbasis teks.

contohnya:

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

## Struktur data list

List adalah salah satu struktur data dalam bahasa pemrograman python. List dapat kita gunakan untuk menyimpan kumpulan objek/nilai, yang kemudian kita sebut sebagai elemen list. Elemen pada list tersimpan menurut urutan (sequence) tertentu. Isi sebuah list dapat dimanipulasi sehingga dapat berubah (mutable). Ini artinya elemen list dapat ditambah maupun dikurangi.


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

## Struktur data set

Set adalah struktur data berisi kumpulan data tak terurut (unordered). Set bersifat mutable, kita dapat menambah maupun mengurangi data yang ada di dalamnya. Elemen di dalam set harus unik, tidak boleh ada duplikasi elemen pada set. Elemen di dalam set harus berupa eleman yang immutable, setiap elemen yang ada tidak boleh berubah (bedakan dengan set-nya sendiri yang mutable). Ini berarti, Elemen set hanya dapat berupa string, number, dan tuple.

contohnya:

    warung_makan = {'sob buntut','soto','bubur','bubur ayam','tongseng'}
    minuman = {'es teh','es jeruk','anggur merah','kopi'}
    pasilitas = {'kamar mandi','kamar tidur','alat yang dibutuhkan','mobil'}
    print(warung_makan)
    print(minuman)
    print(pasilitas)

hasilnya

    {'sob buntut', 'tongseng', 'soto', 'bubur ayam', 'bubur'}
    {'es jeruk', 'anggur merah', 'es teh', 'kopi'}
    {'mobil', 'alat yang dibutuhkan', 'kamar tidur', 'kamar mandi'}

## Struktur data tuple

Tuple adalah struktur data dengan urutan (sequence) tertentu seperti list. Bedanya, bila kita bisa memanipulasi isi sebuah list, kita tidak bisa memanipulasi isi sebuah tuple. Tuple bersifat immutable, isinya tidak dapat kita tambah maupun kurangi.

Sifat immutable dari tuple membuatnya cocok untuk memproteksi struktur data kita dari perubahan. Dengan menggunakan tuple kita mendapatkan jaminan bahwa elemen tidak akan bertambah atau berkurang sejak ia pertama diberikan nilai. Contoh penggunaannya misalnya, saat kita butuh menampung nama-nama bulan. Karena nama bulan bersifat fixed, maka tipe struktur data yang cocok adalah tuple.

Keuntungan lain dari menggunakan tuple adalah kecepatan. Kode di bawah ini adalah cuplikan kode yang diambil dari (quora). Kode ini membandingkan waktu yang dibutuhkan untuk deklarasi list dan tuple dengan elemen yang sama sebanyak masing-masing 1 juta kali. Jalankan untuk melihat perbedaannya.

contohnya:

    nama_bulan = ('januari','februari','maret','april','mei','juni','juli','agustus','oktober','november','desember')
    for bln in nama_bulan:
    print(bln)
 
hasilnya:

    januari
    februari
    maret
    april
    mei
    juni
    juli
    agustus
    oktober
    november
    desember

## Struktur data dictionary

Artikel kali ini akan membahas struktur data dictionary. Berbeda dengan struktur data list dan tuple, yang nilai elemennya dapat diakses menggunakan indeks, nilai elemen pada dictionary dapat diakses melalui key-nya.

Dictionary merupakan struktur data yang berisi kumpulan dari pasangan kunci (key) dan nilai (value) tertentu. Elemen pada dictionary tidak terurut, sehingga tidak dapat diakses menggunakan sequence. Akses terhadap elemen didalamnya diberikan melalui key yang dimiliki tiap elemen. Dictionary bersifat mutable, elemen yang ada di dalamnya dapat ditambah maupun dikurangi.

contohnya: 

    mhs = {
    'nama'  : 'gibran',
    'prodi' : 'ilmu mantik',
    'pembimbing': 'mas hadi',
    'asal': 'suko lilo',
    'julukan': 'gib'
    }
    print(mhs['nama'])
    print(mhs.get('prodi'))

hasilnya:

    gibran
    ilmu mantik
    
    
## Eksepsi (Exception)
Eksepsi terjadi ketika ada sesuatu yang terduga muncul dalam program. Misalnya program anda akan membaca suatu file, namun file tersebut tidak ada. Hal seperti ini ditangani dengan exception.

### Syntax Error
Syntax error, atau dikenal juga sebagai parsing error, adalah error ketika Python memparsing program anda.

        >>> Print 'halo'
          File "<stdin>", line 1
          Print 'halo'
                    ^
        SyntaxError: invalid syntax
        >>> while True print 'Hello world'
          File "<stdin>", line 1
          while True print 'Hello world'
                         ^
        SyntaxError: invalid syntax
 
 ### Exception
Kita akan mencoba / try membaca input dari pengguna. Tekan Ctrl-d apa yang akan terjadi.

        >>> teks = raw_input('Ketikkan sesuatu: ')
        Ketikkan sesuatu: Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        EOFError

Python mengeluarkan eksepsi EOFError yang berarti menemukan simbol end of file (direpresentasikan oleh Ctrl-d) ketika program berharap tidak akan ada.

### Penanganan Exception
Kita dapat menangani eksepsi menggunakan statemen try ... except. Sederhananya kita letakkan statemen yang mungkin mengeluarkan eksepsi kedalam try-block, dan letakan kode penanganan eksepsi kedapam except-block.

        try:
            teks = raw_input('Ketikkan sesuatu: ')
        except EOFError:
            print '\nKenapa sudah EOF?'
        except KeyboardInterrupt:
            print '\nAnda membatalkan operasi'
        else:
            print 'Anda mengetikkan "%s"' % teks

### Mengeluarkan Exception
Anda dapat mengeluarkan eksepsi menggunakan statemen raise dengan menyediakan obyek eksepsi.

Anda dapat membuat eksepsi sendiri dengan membuat class turunan Exception.

        class InputPendekError(Exception):
            "exception jika input terlalu pendek"

        def __init__(self, panjang, minimal):
            Exception.__init__(self)
            self.panjang = panjang
            self.minimal = minimal



        try:
            teks = raw_input('Ketikkan sesuatu: ')
            panjang = len(teks)
            minimal_panjang = 3

            if panjang < minimal_panjang:
                raise InputPendekError(panjang, minimal_panjang)
        except EOFError:
            print '\nKenapa sudah EOF?'
        except KeyboardInterrupt:
            print '\nAnda membatalkan operasi'
        except InputPendekError as e:
            print 'input terlalu pendek: panjang input: %s, minimal: %s' % (e.panjang, e.minimal)
        else:
            print 'Anda mengetikkan "%s"' % teks

Try ... Finally
Ketika anda membaca file dari program anda. Bagaimana anda memastikan file akan ditutup baik ada eksepsi maupun tidak. Anda bisa menggunakan blok finally pada blok try.

import time

        try:
            f = open('coba.txt')
            while True:
                baris = f.readline()
                if len(baris) == 0:
                    # EOF
                    break
                print baris,
                time.sleep(2) # delay 2 detik
        except KeyboardInterrupt:
            print '\nAnda membatalkan operasi'
        finally:
            f.close()
            print '\nfile ditutup.'
    
Statemen with
Mendapatkan resource pada blok try dan melepasnya pada blok finally merupakan pola yang umum ditemukan. Oleh karena itu, anda dapat menggunakan menggunakan statemen with yang menyediakan mekanisme diatas secara otomatis.

        with open('coba.txt') as f:
            for baris in f:
                print baris,



sumber:

<https://koding.alza.web.id/

<https://www.petanikode.com/

<https://www.w3schools.com/python/python_modules.asp





