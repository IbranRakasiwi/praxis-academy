def tukar(lists,i,j):
    lists[i],lists[j]=lists[j], lists[i]
    
def bubbleTugas(listku):
    perubahan = True
    sesi = len(listku) #banyaknya sesi yang digunakan untuk mengecek data dari awal
    while sesi > 1 and perubahan:
        perubahan = False
        j = 1
        while j < sesi:
            if listku[j]<listku[j-1]:
                perubahan = True
                tukar(listku,j,j-1) 
            j+=1
        print(listku)
        #Jika penanda 'perubahan' tidak terjadi maka perulangan berhenti dan artinya data sudah terurut tanpa melakukan perulangan lagi.
        if not perubahan:
            print("hasil akhir = %s" %str(listku))
        sesi-=1
print("==================================================================")
print("Sebelum Bubble Sort")
mylist=[54,26,13,93,17,77,44,31]
print(mylist)
print("Setelah Bubble Sort")
bubbleTugas(mylist)