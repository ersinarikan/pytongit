#parametresiz fonksiyon
def selamla():
    print("MErhaba")
    print("Ne haber")


selamla()
selamla()
a=10
b=20
c=30
#parametre alan fonksiyon
def toplama(x,y,z):
    print("{} + {} + {} = {}".format(x,y,z,x+y+z))

toplama(a,b,c)
toplama(23,45,67)

#parametre alan ve geriye değer döndüren fonksiyon
def kare(x):
    print("kare alınıyor")
    return x*x
print("5 in karesi",kare(5))
k1=kare(3)
print(k1)
print("Program bitti")
