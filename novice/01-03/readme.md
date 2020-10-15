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
            karyawan1 = Karyawan("Sarah", 1000000)
            # Membuat objek kedua dari kelas Karyawan
            karyawan2 = Karyawan("Budi", 2000000)

            karyawan1.tampilkan_profil()
            karyawan2.tampilkan_profil()
            print("Total karyawan :", Karyawan.jumlah_karyawan)

hasilnya:
            Nama : Sarah
            Gaji : 1000000
            Nama : Budi
            Gaji : 2000000
            Total karyawan : 2

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


