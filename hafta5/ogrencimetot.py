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
    print("isim",ad[i])
    print("Vize notu: ",vn[i])
    print("Final notu",fn[i])
    print("Başarı notu: "bn[i])

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
        aranacakAd=input("Aranacak ismi giriniz: ")
    elif menu==3:
        pass
    elif menu==4:
        pass
    elif menu==5:
        pass
    elif menu==6:
        pass
    elif menu==7:
        print("Program bitti")
        exit(0)
    else:
        print("Yanlış seçim yaptınız")