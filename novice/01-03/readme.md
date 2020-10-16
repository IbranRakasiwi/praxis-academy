## OOP (Object-Oriented Programming)
  
    Hari ketiga

### Apa itu Object-Oriented Programming (OOP)?

Pemrograman berorientasi objek atau dalam bahasa inggris disebut Object Oriented Programming (OOP) adalah paradigma atau teknik pemrograman di mana semua hal dalam program dimodelkan seperti objek dalam dunia nyata. Objek di dunia nyata memiliki ciri atau attribut dan juga aksi atau kelakuan (behaviour).

misalkan sebuah mobil. Mobil memiliki sebuah punya ban, stang, kursi, pedal gas, rem, dan lain sebagainya. Ada juga ciri warna, atau tahun keluaran berapa. Selain punya ciri, mobil juga punya aksi atau sesuatu yang bisa dilakukan olehnya. Misalnya, ketika pedal diinjak apa yang terjadi. Ketika di rem apa yang terjadi, dan lain sebagainya.

Program juga demikian. Semua unit dalam program bisa dianggap sebagai objek. Objek besar dibangun dari objek – objek yang lebih kecil. Objek yang satu berinteraksi dengan objek yang lain, sehingga semua menjadi sebuah kesatuan yang utuh.

Python dari awal dibuat sudah mengadopsi OOP. Selain itu Python juga bisa menggunakan paradigma pemrograman lama yaitu pemrograman terstruktur. Oleh karena itu, Python disebut bersifat hibrid.

Pembuatan Kelas

Kita mendefinisikan sebuah kelas dengan menggunakan kata kunci class diikuti oleh nama kelas tersebut. Berikut adalah sintaks pembuatan kelas di Python.

    class Karyawan:
    '''Dasar kelas untuk semua karyawan'''
        jumlah_karyawan = 0

        def __init__(self, nama, gaji):
            self.nama = nama
            self.gaji = gaji
            Karyawan.jumlah_karyawan += 1

        def tampilkan_jumlah(self):
            print("Total karyawan:", Karyawan.jumlah_karyawan)

        def tampilkan_profil(self):
            print("Nama :", self.nama)
            print("Gaji :", self.gaji)

    # Membuat objek pertama dari kelas Karyawan
    karyawan1 = Karyawan("gibran", 1000000)
    # Membuat objek kedua dari kelas Karyawan
    karyawan2 = Karyawan("adi", 2000000)
    # Membuat objek keketiga dari kelas Karyawan
    karyawan3 = Karyawan("alan", 2000000)

    karyawan1.tampilkan_profil()
    karyawan2.tampilkan_profil()
    karyawan3.tampilkan_profil()
    print("Total karyawan :", Karyawan.jumlah_karyawan)




hasilnya:

            Nama : gibran
            Gaji : 1000000
            Nama : adi
            Gaji : 2000000
            Nama : alan
            Gaji : 2000000
            Total karyawan : 3

Variabel jumlah_karyawan adalah variabel kelas yang dibagi ke semua instance/objek dari kelas ini. Variabel ini bisa diakses dari dalam atau luar kelas dengan menggunakan notasi titik, Karyawan.jumlah_karyawan.

Metode __init__() adalah metode konstruktor, yaitu metode khusus yang digunakan Python untuk menginisialisasi pembuatan objek dari kelas tersebut.

Fungsi – fungsi di dalam kelas (disebut metode) pendefinisiannya sama dengan fungsi pada umumnya. Hanya saja, harus ada argumen pertama bernama self. Pada saat pemanggilan fungsi, argumen ini otomatis ditambahkan oleh Python. Anda tidak perlu menambahkannya pada saat memanggil fungsi.


## CARD CRC
CRC adalah kumpulan kartu indeks standar yang telah dibagi menjadi tiga bagian (class,responsibilities, collaborator). Class merupakan koleksi benda-benda yang sama, responsibilities adalah sesuatu yang diketahui class atau tidak, dan collaborator yang berinteraksi untuk mengisi dari responsibilities.

Responsibilities dan Collaborators

Model Class Responsibility Collaborator (CRC) adalah kumpulan kartu indeks standar yang telah dibagi menjadi tiga bagian.

    1. Kelas mewakili kumpulan objek serupa,
    2. Responsibiliti adalah sesuatu yang diketahui atau dilakukan oleh class, dan
    3. kolaborator adalah kelas lain yang berinteraksi dengan class untuk memenuhi Responsibiliti.



## class

Class adalah ‘cetak biru’ atau ‘blueprint’ dari object. Class digunakan hanya untuk membuat kerangka dasar. Yang akan kita pakai nantinya adalah hasil cetakan dari class, yakni object.

Class di dalam OOP di gunakan untuk membuat sebuah kerangka kerja. bisa di katakan sebagai library. class berisi property dan method. jadi ibaratnya class adalah sebuah wadah yang menyimpan property dan method. dan object yang dihasilkan biasanya berdasarkan isi dari class. jika kita ibaratkan lagi. di dalam OOP PHP. class di tulis dengan awalan syntax class. dan kemudian baru di ikuti dengan nama class nya.

berikut contoh class:

    class MyClass:
     int = 1,2,3,4,5,6,7,8,9,10,11
    p1 = MyClass()
    print(p1.int)
    
hasilnya:

  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
  
contoh lagi:

    class Person:
      def __init__(self, nama, umur, kuliah):
        self.nama = nama
        self.umur = umur
        self.kuliah = kuliah

    p1 = Person("gibran", 24, "UNU Jogja" )

    print(p1.nama)
    print(p1.umur)
    print(p1.kuliah)

Hasilnya:

    gibran
    24
    UNU Jogja
  
Fungsi __init __ ()

Contoh di atas adalah kelas dan objek dalam bentuk yang paling sederhana,

Untuk memahami arti dari kelas kita harus memahami fungsi built-in __init __ ().

Semua kelas memiliki fungsi yang disebut __init __ (), yang selalu dijalankan saat kelas sedang dimulai.

Gunakan  fungsi __init __ () untuk menetapkan nilai nama, usia dan kuliah.

**Ubah Properti Objek**

Anda dapat mengubah properti pada objek seperti ini:

Contoh
Atur usia p1 menjadi 19.

      p1.age = 19

**Hapus Properti Objek**

Anda dapat menghapus properti pada objek dengan menggunakan delkata kunci:

Contoh

Hapus properti kuliah dari objek p1:

    del p1.kuliah

### Menggunakan Standard Library Python

Standard Library adalah kumpulan modul yang mempermudah dalam melakukan tugas tertentu untuk menghasilkan solusi dari suatu permasalahan tertentu.

Standard library ini sudah termasuk dalam instalasi Python, kita tidak perlu menambahkan atau mendownload lagi.

Sebagai contoh, kita dapat melakukan cukup banyak hal dengan standard library Python
  - Program untuk melakukan backup rutin pada Linux, Solaris dan Mac, library standard yang dapat digunakan adalah os, stat, bz2, gzip, time, datetime, tar dan optparse
  - Program Apache log file analysis tool menggunakan modul optparse, urlparse, cgi, datetime, operator, re, sys, and mmap.
  - Program sederhana web API clients cukup menggunakan library urllib/urllib2, ElementTree, dan xml package
  - Program MySQL backup script menggunakan sys, os, time, shutil, glob, tarfile, dan optparse modules.




