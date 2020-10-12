# AWAL PYTHON
Hari pertama 

Bahasa pemrograman adalah bahasa baku yang terdiri dari sekumpulan peraturan untuk memerintah komputer. Bahasa pemrograman menurut tingkat kedekatannya dengan mesin komputer terdiri dari:

Bahasa Mesin, berupa bahasa biner contoh 10110101010 Bahasa Tingkat Rendah, berupa bahasa dengan kode-kode singkat contoh MOV, SUB, CMP, JMP, JGE, JL, LOOP, dsb. Bahasa Tingkat Tinggi, bahasa komputer memakai atribut yang berasal dari kata-kata bahasa manusia, contohnya begin, end, if, for, while, and, or, dsb. Karena bahasa yang berhubungan dengan komputer adalah bahasa mesin, maka diperlukan compiler atau interpreter agar semua dapat informasi ke dalam bahasa mesin. Compiler adalah program yang mengkompilasi semua kode sumber, kode sumber terlebih dahulu dibaca compiler dan tidak ada kesalahan maka kode sumber dirubah menjadi program yang dapat dijalankan. Interpreter berfungi menterjemahkan kode sumber secara baris perbaris kedalam bahasa mesin sekaligus dieksekusi, lalu masuk ke dalam kode sumber maka program interpreter seketika.

**Apa itu Python?**

Python merupakan bahasa pemrograman tingkat tinggi yang diracik oleh Guido van Rossum.

Python banyak digunakan untuk membuat berbagai macam program, seperti: program CLI, Program GUI (desktop), Aplikasi Mobile, Web, IoT, Game, Program untuk Hacking, dsb.

Python juga dikenal dengan bahasa pemrograman yang mudah dipelajari, karena struktur sintaknya rapi dan mudah dipahami.

(Python bagus untuk pemula yang belum pernah coding).

**Kenapa belajar Python?**

1. cepat dan efectif
2. Mudah dipelajari
3. banyak digunakan di perusahan besar


Karena tugas kita ada beberapa diantaranya mengistal python, pip, jupyter. berikut cara mengistalnya:

**Cara cek python apakan udah teristal**

Pertama untuk mengecek python yang persi biasa sebagai berikut:

$ python --version

sedangkan untuk mngecek yang ke versi yang ke tiga sebagai berikut:

$ python3 --version

**cara mengistal pip**

kita cek terlebih dahulu apakah pip udah teristal apakah belum, caranya masih sama saja seperti python tadi. sebelum mwngistal pip, terlebih dahulu kita mencari tau apa sih pip itu?

PIP merupakan program untuk manajemen paket di Python. Tugasnya untuk menginstal, menghapus, upgrade paket Python, dll.

Paket Python itu apa?

Paket Python itu merupakan sebuah modul yang berisi kode-kode python dan isi paket ini bisa kita impor ke dalam program kita.

Kamu juga bisa membuat sendiri paket Python, lalu menyebarkannya ke seluruh dunia. Sehingga programmer yang lain bisa memanfaatkannya.


**untuk mengistal pip dengan perintah**

$ sudo apt-get install python3-pip

nha udah pada taukan caranya? yuk kita lanjut ke jupyter. nah sebelum kita lanjut cara mengistal jupyter kita terlebih dahulu mencari tau apasih jupyter itu?

JupyterLab adalah lingkungan pengembangan interaktif berbasis web untuk notebook, kode, dan data Jupyter. JupyterLab fleksibel: mengonfigurasi dan mengatur antarmuka pengguna untuk mendukung berbagai alur kerja dalam ilmu data, komputasi ilmiah, dan pembelajaran mesin. JupyterLab dapat dikembangkan dan modular: plugin tulis yang menambahkan komponen baru dan terintegrasi dengan yang sudah ada.

nah udah pada tahukan jupyter itu apa. nah kita lanjut untuk mengistal jupyter caranya seperti ini.

$pip3 install jupyterlab

atau menggunkan 

$python3 -m pip install jupyterlab

untuk mengecek apakah jupyter kita udah teristal apa belum. caranya seperti ini

$ jupyter lab

nah udah pada tahukan python itu apa?, pip, dan jupyter. dan udah pad tau jugakan cara instalnya.


**mode interactive di Python**

Python memiliki dua mode dasar: skrip dan interaktif. Mode normal adalah mode di mana file skrip dan .pyfile jadi dijalankan dalam interpreter Python. Mode interaktif adalah shell baris perintah yang memberikan umpan balik langsung untuk setiap pernyataan, saat menjalankan pernyataan yang sebelumnya dimasukkan dalam memori aktif. Saat baris baru dimasukkan ke penerjemah, program makan dievaluasi baik sebagian maupun seluruhnya.

Mode interactive adalah cara yang baik untuk bermain-main dan mencoba variasi sintaks.

Di macOS atau linux, buka terminal dan cukup ketik "python". Di Windows, buka prompt perintah dan ketik "py", atau mulai sesi Python interaktif dengan memilih "Python (baris perintah)", "IDLE", atau program serupa dari bilah tugas / menu aplikasi. IDLE adalah GUI yang menyertakan mode interaktif dan opsi untuk mengedit dan menjalankan file.

Python harus mencetak sesuatu seperti ini:

$ python
Python 3.0b3 (r30b3: 66303, 8 Sep 2008, 14:01:02) [MSC v.1500 32 bit (Intel)] pada win32
Ketik "bantuan", "hak cipta", "kredit" atau "lisensi" untuk informasi lebih lanjut.
>>>

**1 Bubble Sort**

Yang pertama kita akan membahas bubble sort. Algoritma ini merupakan salah satu algoritma pengurutan yang paling sederhana, baik dalam hal pengertian maupun penerapannya.
Berikut ini adalah gambaran dari algoritma bubble sort:

for i:=1 to Jumlah_data-1 do
  for j:=i+1 to Jumlah_data do
    if Data[i]>Data[j] then
    begin
      t:=Data[i];
      Data[i]:=Data[j];
      Data[j]:=t;
    end;

Kita misalkan memiliki 5 angka yang akan kita simpan kedalam variabel Data (Array).

Dengan masing-masing nilai sebagai berikut:

Data[1] := 3;
Data[2] := 1;
Data[3] := 4;
Data[4] := 2;
Data[5] := 6;

**Quick Short**

Algoritma quick short ditemukan oleh E. Hoare. Algoritma ini menggunakan metode rekursi sampai habis. Prinsipnya membagi data menjadi dua bagian yang sama (kiri dan kanan).

Dimana data tengah menjadi pivot (pusat operasi). Kemudian kita akan mengumpukan data dengan nilai lebih kecil dari pivot disebelah kiri pivot, dan di kanan untuk yang lebih besar.

Karena dimungkinkan bagian kiri dan kanan pivot tidak sama besarnya. maka dari itu tiap bagian di bagi menjadi dua lagi sehingga mempunyai pivot yang baru.

baca:=0;
pusat := A[(awal+akhir) div 2];
kiri := awal;
kanan := akhir;
While kiri <= kanan Do
  Begin
  While A[kiri] < pusat Do
  Inc(kiri);
  While A[kanan] > pusat Do
    Dec(kanan);
    If kiri<=kanan Then
      Begin
      Ganti(A[kiri],A[kanan]);
      Inc(kiri);
      Dec(kanan);
      Inc(baca);
      End;
  End;

If kanan>awal Then
  Urut(awal,kanan);
  If akhir>kiri Then
    Urut(kiri,akhir);
    
    
Algoritma Quick Sort juga disebut juga dengan partition Exchange sort karena konsepnya membuat partisi-partisi, dan sort dilakukan per partisi.


**Shell Sort**

Prinsipnya hampir sama dengan Bubble Sort tetapi dioptmisisasi sehingga lebih cepat.

Ditemukan oleh Donald Shell. prinsipnya adalah membandingkan data dengan jarak tertentu dalam array. Algoritma utamanya adalah sebagai berikut :

baca:=0;
For i:= (m Div 2) Downto 1 Do
For j:= 1 To m-i Do
  If A[j]>A[j+i] Then
  Begin
    Ganti(A[j],A[j+i]);
    Inc(baca);
  End;

**Selection Sort**

Algoritma utamanya adalah sebagai berikut:

baca:=0;
For i:= 1 To m-1 Do
Begin
  tempat:=i;
  For j:= i+1 To m Do
    If A[tempat]>A[j] Then
      tempat:=j;
      Ganti(A[i],A[tempat]);
      Inc(baca);
End;

**5 Insert Sort**

Algoritma utamanya adalah sebagai berikut :

baca:=0;
For i:= 2 To m Do
Begin
  G:=A[i];
  j:=i-1;
  A[0]:=G;
    While G<A[j] Do
    Begin
      A[j+1]:=A[j];
      Dec(j);
      Inc(baca);
    End;
    A[j+1]:=G;
End;

**Demikian. Terimakasih**

