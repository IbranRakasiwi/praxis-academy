class Stack:
    def __init__(self):
        self.items=[]
        
    def isEmpty(self):
        return self.items == []
    def open(self):
        return self.items
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    
s = Stack()

stak=[]
soal =''
pasangan = [['siang','malam'],['terang','gelap'],['malam','siang'],['gelap','terang'],['terbit','tenggelam'],['tenggelam','terbit']]
masukan = int(input('Masukan berapa banyak kata yang ingin diinput = '))
for i in range(masukan):
    b = input('Masukan kata ke %i = '%(i+1))
    s.push(b)
    stak.append(b)
for i in range(len(stak)):
    soal=soal + stak[i] + ' '
#print(s.open())
hasil = 0
pembanding = False
hasil1 = False
while not s.isEmpty():
    a = Stack()
    if len(s.open()) == 1:
        hasil1=False
    cek = s.pop()
    for i in range(len(pasangan)):
        pas = pasangan[i][0]
        if cek == pas:
            ketemu = False
            if s.size() <= 0:
                ketemu = True
            else:
                ketemu = False
            while not ketemu:
                ka = s.open()
                jum = len(ka)-1
                while jum >= 0:
                    cek1 = ka[jum]
                    if pasangan[i][1] == cek1:
                        ketemu = True
                        hasil1 = True
                        ka.remove(cek1)
                        break
                    else:
                        hasil1 = False
                    jum-=1
                ketemu = True
    hasil = hasil1
    pembanding = hasil and hasil1
print(soal +'-> '+ str(pembanding))

print('')
print('')
print('')
        
