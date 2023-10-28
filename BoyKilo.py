boy=float(input("Boy Değeri Metre Olarak Giriniz : "))
kilo=float(input("Kilo Değeri Giriniz : "))
vke=kilo/(boy*boy)
sonuc=""
if (vke<18.5):
    sonuc="ideal kilonun altındasın"
#elif vke>=18.5 and vke<25:
elif vke<25:
    sonuc="ideal kilodasın"
elif vke<30:
    sonuc="ideal kilonun üstündesin"
elif vke<40:
    sonuc="Obez"
else:
    sonuc="morbid obez"
print("boyun : ",boy,"Kilon : ",kilo,"vke değerin",vke,"durumun",sonuc)
