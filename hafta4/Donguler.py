#in operatörü içindemi
# print("a" in "Ankara")
# print("d" in "Ankara")
# print("mer" in "merhaba")
liste=[1,4,7,3,8,2,9,15,35,66,88,23]
# toplam=0
# for eleman in liste:
#     print("sayi",eleman)
#     toplam=toplam+eleman
# print("toplam : ",toplam)
# print("Ortalama",(toplam//len(liste)))
# print("break işlemi")
# for eleman in liste:
#     print(eleman)
#     if eleman==3:
#         break
# print("continue işlemi")
# print(liste)
# for eleman in liste:
#     if eleman%2==0:
#         continue
#     print(eleman)
print(liste)
tekListe=[]
ciftListe=[]
for sayi in liste:
    if sayi%2==0:
        ciftListe.append(sayi)
    else:
        tekListe.append(sayi)
print("tek sayıların listesi :",tekListe)
print("Çift sayıların listesi :",ciftListe)
ad=["Ali","Veli","Ayşe","fatma"]
for isim in ad:
    print(isim)
print("bitti")
okulAdi="Okan üniversitesi"
for karakter in okulAdi:
    print(karakter)
liste=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
print(liste[0])
print(liste[0][0])
for i,j,k in liste:
    print("i",i,"j",j,"k",k)
sozluk={"bir":1,"iki":2,"uc":3}
for (anahtar, deger) in sozluk.items():
    print(anahtar,deger)
print(sozluk.items())
