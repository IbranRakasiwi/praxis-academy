# mendefinisikan fungsi `panggilan` di mana Anda menyediakan fungsi dan argumennya
def call(x, f):
    return f(x)

# mendefinisikan fungsi yang mengembalikan kotak
square = lambda x : x*x

# mendefinisikan fungsi yang mengembalikan kenaikan
increment = lambda x : x+1

# mendefinisikan fungsi yang mengembalikan kubus
cube = lambda x : x*x*x

# mendefinisikan fungsi yang mengembalikan penurunan tersebut
decrement = lambda x : x-1

# letakkan semua fungsi dalam daftar sesuai urutan yang Anda inginkan untuk menjalankannya
funcs = [square, increment, cube, decrement]

# satukan semuanya. Di bawah ini adalah bagian non fungsional.
# dalam pemrograman fungsional Anda memisahkan bagian fungsional dan non fungsional.
from functools import reduce # reduce ada di pustaka functools
print(reduce(call, funcs, 96)) # output 783012621312