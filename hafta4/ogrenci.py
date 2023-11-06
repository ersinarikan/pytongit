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
toplam = 0
for bnNot in bn:
    toplam += bnNot
bnOrt=toplam / kisi
while True:
    menu=int(input("""
    1-Listeleme
    2-Vize ortalama
    3-Final Ortalama
    4-Başarı Ortalama
    5-başarı not ortalamadan büyük bilgi 
    6-En büyük başarı notu
    7-En küçük başarı notu ve kime ait
    8-İsim arama
    9-Çıkış"""))
    if menu==1:
        for i in range(kisi):
            print("Adı : ",ad[i])
            print("Vize notu {}\tFinal notu {}\tBaşarı notu {}".format(vn[i],fn[i],bn[i]))
            print("Vize Notu",vn[i],"\tFinal notu",fn[i],"\tBaşarı notu",bn[i])
            print("-"*50)
    elif menu==2:
        toplam=0
        for vNot in vn:
            toplam+=vNot
        print("Vize Not ortalaması : ",(toplam/kisi))
    elif menu==3:
        toplam = 0
        for fNot in fn:
            toplam += fNot
        print("Final Not ortalaması : ", (toplam / kisi))
    elif menu==4:
        print("Başarı Not ortalaması : ", bnOrt)
    elif menu==5:
        for i in range(kisi):
            if bn[i]>bnOrt:
                print("Adı : ", ad[i])
                print("Vize notu {}\tFinal notu {}\tBaşarı notu {}".format(vn[i], fn[i], bn[i]))
                print("-" * 50)
    elif menu==6:
        enb=bn[0]
        for i in range(1,kisi):
            if bn[i]>enb:
                enb=bn[i]
        print("en büyük başarı notu : ",enb)
    elif menu==7:
        enk=bn[0]
        for i in range(1,kisi):
            if bn[i]<enk:
                enk=bn[i]
        print("en küçük başarı notu : ",enk)
        for i in range(kisi):
            if bn[i]==enk:
                print("Adı : ", ad[i])
                print("Vize notu {}\tFinal notu {}\tBaşarı notu {}".format(vn[i], fn[i], bn[i]))
                print("-" * 50)
    elif menu==8:
        kontrol=False
        aranacakIsim=input("İsim giriniz : ")
        for i in range(kisi):
            if aranacakIsim==ad[i]:
                kontrol=True
                print("Adı : ", ad[i])
                print("Vize notu {}\tFinal notu {}\tBaşarı notu {}".format(vn[i], fn[i], bn[i]))
                print("-" * 50)
        if kontrol==False:
            print("Aranan isim listede yok")
    elif menu==9:
        print("Program bitti")
        exit(0)
    else:
        print("Yanlış menü değeri")

