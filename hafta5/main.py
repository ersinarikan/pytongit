ad=[]
maas=[]
yas=[]
cinsiyet=[]
kisi=int(input("kişi sayısını giriniz:" ))
for i in range(kisi):
    ad.append(input("isim giriniz:" ))
    maas.append(input("maas miktarını giriniz: "))
    cinsiyet.append(input("cinsiyet giriniz (E/H): "))
    yas.append(int(input("Yaşı: ")))
# print("ad",ad)

# print("maas",maas)

# print("cinsiyet",cinsiyet)

while True:

    menu=int(input("""

    1-Listeleme

    2-Toplam Maas ortalama

    3-Erkelerin Maaş Ortalaması

    4-Kadınların Maaş Ortalaması

    5-Toplam Maaş Ortalaması 

    6-En büyük Yaş

    7-En küçük Yaş

    8-Toplam Yaş Ortalaması

    9-Erkelerin Yaş Ortalaması

    10-Kadınların Yaş Ortalaması

    11-Çıkış"""))

    if menu==1:

        for i in range(kisi):

            print("-" * 50)

            print("Adı : ",ad[i])

            print("Maas {}\tCinsiyet {}\tYas {}".format(maas[i],cinsiyet[i],yas[i]))

            print("-"*50)

    elif menu==2:

        toplam=0

        for i in range(kisi):

            toplam=toplam+maas[i]

            print("Maas Ortalama: ",(toplam/kisi))

    elif menu==3:

        toplam=0

        sayac=0

        #for i in range(0,(kisi-1)):

        for i in range(kisi):

            if cinsiyet[i]=='E' or cinsiyet[i]=='e':
                print("toplam tipi",type(toplam),"maas tipi",type(maas[i]))
                toplam=toplam+maas[i]


                #print("Toplam", toplam)

                sayac=sayac+1

                #print("sayac",sayac)

        print("Erkeklerin maaş ortalaması: ",(toplam/sayac))

