ad=input("İsim Giriniz")
vNot=int(input("Vize Notu Giriniz : "))
fNot=int(input("Final Notu Giriniz : "))
bNot=vNot*0.4+fNot*.6

durum=""
if bNot<50:
    durum="Kaldın"
else:
    durum="Geçtin"
print(ad,"Başarı notun",bNot,durum)
