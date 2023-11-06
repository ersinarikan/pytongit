ad = []
maas = []
yas = []
cinsiyet = []
kisi = int(input("kişi sayısını giriniz:"))
for i in range(kisi):
    ad.append(input("isim giriniz: "))
    maas.append(int(input("maas miktarını giriniz: ")))
    cinsiyet.append(input("cinsiyet giriniz (E/B): "))
    yas.append(int(input("Yaşı: ")))
# print("ad",ad)
# print("maas",maas)
# print("cinsiyet",cinsiyet)
while True:
    menu = int(input("""
    1-Listeleme
    2-Toplam Maas ortalama
    3-Erkelerin Maaş Ortalaması
    4-Kadınların Maaş Ortalaması
    5-En büyük Yaş
    6-En küçük Yaş
    7-Toplam Yaş Ortalaması
    8-Erkelerin Yaş Ortalaması
    9-Kadınların Yaş Ortalaması
    10-Çıkış"""))
    if menu == 1:
        for i in range(kisi):
            print("-" * 50)
            print("Adı : ", ad[i])
            print("Maas {}\tCinsiyet {}\tYas {}".format(maas[i], cinsiyet[i], yas[i]))
            print("-"*50)
    elif menu == 2:
        toplam = 0
        for i in range(kisi):
            toplam = toplam+maas[i]
            print("Maas Ortalama: ", (toplam/kisi))
    elif menu == 3:
        toplam = 0
        sayac = 0
        for i in range(kisi):
            if cinsiyet[i] == 'E' or cinsiyet[i] == 'e':
                toplam = toplam+maas[i]
                sayac = sayac+1
        print("Erkeklerin maaş ortalaması: ", (toplam/sayac))
    elif menu == 4:
        toplam = 0
        sayac = 0
        for i in range(kisi):
            if cinsiyet[i] == 'K' or cinsiyet[i] == 'k':
                toplam = toplam+maas[i]
                sayac = sayac+1
        print("Kadınların maaş ortalaması: ", (toplam/sayac))
    elif menu == 5:
        eby = yas[0]
        for i in range(kisi):
            if yas[i] > eby:
                eby = yas[i]
        print("En büyük yaş: ", eby)
    elif menu == 6:
        eky = yas[0]
        for i in range(kisi):
            if yas[i] > eky:
                eky = yas[i]
        print("En küçük yaş: ", eky)
    elif menu == 7:
        toplam = 0
        for i in range(kisi):
            toplam = toplam + yas[i]
        print("Toplam Yaş Ortalamsı: ", (toplam/kisi))
    elif menu == 8:
        toplam = 0
        sayac = 0
        for i in range(kisi):
            if cinsiyet[i] == 'E' or cinsiyet[i] == 'e':
                toplam = toplam+yas[i]
                sayac = sayac+1
        print("Erkeklerin Yaş ortalaması: ", (toplam/sayac))
    elif menu == 9:
        toplam = 0
        sayac = 0
        for i in range(kisi):
            if cinsiyet[i] == 'K' or cinsiyet[i] == 'k':
                toplam = toplam+yas[i]
                sayac = sayac+1
        print("Kadınların yaş ortalaması: ", (toplam/sayac))
    elif menu == 10:
        print("Program Bitti")
    else:
        exit(0)


