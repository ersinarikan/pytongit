print(*range(20,10,-2))
print(range(10))
#başlangıcı hep sıfır alır
print(*range(10))
#tek yazarsan 0 dan başlar 2 yazarsan başlangıç ve bitiş değeri 3 karakter yazarsan başlangıç bitiş ve artışdeğeri

sayilar=[10,20,3,45,67,34]
toplam=0
for sayi in sayilar:
    toplam+=sayi
print("toplamları ", toplam)
print("ortalaması", toplam/len(sayilar))
toplam1=0
for i in range(0,len(sayilar)):
    toplam1=toplam1+sayilar[i]
print("toplamları", toplam1)
print("ortalaması", toplam1/len(sayilar))




