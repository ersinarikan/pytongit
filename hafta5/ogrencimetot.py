ad=list()
vn=[]
fn=[]
bn=[]
kisi=int(input("Kişi sayısı giriniz : "))
for i in range(kisi):
    ad.append(input("isim giriniz"))
    vnGecici=int(input("Vize notu giriniz : "))
    vn.append(vnGecici)
    fnGecici = int(input("Final notu giriniz : "))
    fn.append(fnGecici)
    bn.append((vnGecici*0.4+fnGecici*0.6))
def listele(ad,vn,fn,bn):
    for i in range(len(ad)):
        print("isim : ", ad[i])
        print("vize notu :" ,vn[i])
        print("final notu :" , fn[i])
        print("başarı notu : " ,bn[i])
        print("-"*40)


def arama(aranacakAd, ad, bn, kisi):
    for i in range(len(ad)):
        if aranacakAd==(ad[i]):
            print("İsim", ad[i])
            print("Vize Notu : ", vn[i])
            print("Final Notu : ", fn[i])
            print("Başarı Notu : ", bn[i])
            print("-"*40)


def ortalama(notlar):
    toplam=0
    for sayi in notlar:
        toplam+=sayi
    return (toplam/len(notlar))


def enb(notlar):
    enBuyuk=notlar[0]
    for i in range(len(notlar)):
        if notlar[i]>enBuyuk:
            enBuyuk=notlar[i]
    return enBuyuk


def enk(notlar):
    enKucuk=notlar[0]
    for veri in (notlar):
        if (veri<enKucuk):
            enKucuk=veri
    return enKucuk


def enBuyukBasari(ad, vn, fn, bn):
    enbBasari=enb(bn)
    for i in range(len(ad)):
        if bn[i]==enbBasari:
            print("İsim", ad[i])
            print("Vize Notu : ", vn[i])
            print("Final Notu : ", fn[i])
            print("Başarı Notu : ", bn[i])


while True:
    menu=int(input("""
    1-Listeleme
    2-İsim Arama
    3-Vize Final Basarı Notu Ortalama
    4-Tümünün En Büyüğü
    5-Tümünün En Küçüğü
    6-En büyük başarı notu kime ait
    7-Çıkış"""))
    if menu==1:
        listele(ad,vn,fn,bn)
    elif menu==2:
       aranacakAd=("Aranacak ismi giriniz :")
       arama(aranacakAd,ad,bn,kisi)
    elif menu==3:
        print("Vize Not Ortalaması : ", ortalama(vn))
        print("Final Not Ortalaması : ", ortalama(fn))
        print("Başarı Not Ortalaması : ", ortalama(bn))

    elif menu==4:
        print("Vize en büyük: ", enb(vn))
        print("Final en büyük: ", enb(fn))
        print("Başarı en büyük: ", enb(bn))
    elif menu==5:
        print("Vize en küçük: ", enk(vn))
        print("Final en küçük: ", enk(fn))
        print("Başarı en küçü: ", enk(bn))
    elif menu==6:
        enBuyukBasari(ad,vn,fn,bn)
        enbBasari=enb(bn)
        print("en büyük",enbBasari)
    elif menu==7:
        print("Program bitti")
        exit(0)
    else:
        print("Yanlış seçim yaptınız")