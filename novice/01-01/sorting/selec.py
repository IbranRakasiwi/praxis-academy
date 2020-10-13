def tukar(lists,i,j):
   lists[i],lists[j]=lists[j],lists[i]
   
def tugasSelection(listku):
   perubahan = True
   sesi = 0 #digunakan untuk membuat sesi pencarian
   while sesi < len(listku)-1 and perubahan:
       perubahan = False
       indeksTerendah = sesi
       indeksLanjutan = indeksTerendah + 1
       while indeksLanjutan < len(listku):
           if listku[indeksTerendah] > listku[indeksLanjutan]:
               indeksTerendah = indeksLanjutan
           indeksLanjutan += 1
       if indeksTerendah != sesi:
           tukar(listku,indeksTerendah,sesi)
           perubahan = True
       print(listku)  
       #Jika penanda 'perubahan' tidak terjadi maka perulangan berhenti dan artinya data sudah terurut tanpa melakukan perulangan lagi.
       if not perubahan:
           print("hasil akhir = %s" %str(listku))
       sesi += 1
print("=========================================================")
print('Sebelum Selection Sort')
listku = [54,26,13,93,17,77,44,31]
print(listku)
print("Setelah Selection Sort")
tugasSelection(listku)
print("=========================================================")