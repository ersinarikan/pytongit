ad=list()
vn=[]
fn=[]
bn=[]
kisi=int(input("Kişi sayısı giriniz : "))
for i in range(kisi):
  ad.append(input("İsim Giriniz : "))
  vnGecici=int(input("Vize Notu Giriniz : "))
  vn.append(vnGecici)
  fnGecici=int(input("Final Notu Giriniz : "))
  fn.append(fnGecici)
  bn.append(vnGecici*.4+fnGecici*.6)

def liste(isim, vizeNot, finalNot, basariNot):
    print("İsminiz : ",isim)
    print("Vize notu : ",vizeNot)
    print("Final notu : ",finalNot)
    print("Başarı notu : ",basariNot)
    print("-"*40)

def listele(ad, vn, fn, bn):
    for i in range(len(ad)):
        liste(ad[i],vn[i],fn[i],bn[i])

def arama(aranacakAd, ad, bn, kisi):
    for i in range(len(ad)):
        if aranacakAd==ad[i]:
            liste(ad[i],vn[i],fn[i],bn[i])



def ortalama(notlar):
    toplam=0
    for sayi in notlar:
        toplam+=sayi
    return toplam/len(notlar)


def enb(notlar):
    enBuyuk=notlar[0]
    for i in range(len(notlar)):
        if notlar[i]>enBuyuk:
            enBuyuk=notlar[i]
    return enBuyuk


def enk(notlar):
    enKucuk=notlar[0]
    for veri in notlar:
        if(veri<enKucuk):
            enKucuk=veri
    return enKucuk


def enBuyukBasari(ad, vn, fn, bn):
    enbBasari=enb(bn)
    for i in range(len(ad)):
        if bn[i]==enbBasari:
            liste(ad[i],vn[i],fn[i],bn[i])

while True:
    menu=int(input("""
    1 - Listeleme 
    2 - İsim arama
    3 - Vize,fn, bn ortalama
    4 - Tümünün en büyüğü
    5 - Tümünün en küçüğü
    6 - En büyük başarı kime ait
    7-Çıkış"""))
    if menu==1:
        listele(ad,vn,fn,bn)
    elif menu==2:
        aranacakAd=input("Aranacak ismi giriniz : ")
        arama(aranacakAd,ad,bn,kisi)
    elif menu==3:
        print("Vize not ortalaması : ",ortalama(vn))
        print("Final not ortalaması : ",ortalama(fn))
        print("Başarı not ortalaması : ",ortalama(bn))
    elif menu==4:
        print("en büyük vize",enb(vn))
        print("en büyük final",enb(fn))
        print("en büyük başarı",enb(bn))
    elif menu==5:
        print("en küçük vize",enk(vn))
        print("en küçük final",enk(fn))
        print("en küçük başarı",enk(bn))
    elif menu==6:
        enBuyukBasari(ad,vn,fn,bn)

    elif menu==7:
        print("program bitti")
        exit(0)
    else:
        print("yanlış menü değeri")




