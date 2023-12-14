tekrar = 'E'


def liste(yazarismi, kitapismi, sayfasayisi, cinsiyeti):
    if cinsiyeti == 'e':
        cinsiyeti = "ERKEK"
    else:
        cinsiyeti = "KADIN"
    print("-" * 50)
    print("Yazar İsmi: ", yazarismi.upper())
    print("Kitap İsmi: ", kitapismi.upper())
    print("Sayfa Sayısı: ", sayfasayisi)
    print("Cinsiyet: ", cinsiyeti)


def listele(ad, kitap, sayfa, cinsiyet):
    for i in range(len(ad)):
        liste(ad[i], kitap[i], sayfa[i], cinsiyet[i])


def liste2(adlar, kitaplar):
    print("-" * 50)
    print("Yazar İsmi: ", adlar.upper())
    print("Kitap İsmi: ", kitaplar.upper())


def listele2(adlar, kitaplar):
    for i in range(len(ad)):
        liste2(ad[i], kitap[i])


def liste3(yazarAdi, cinsiyeti):
    if cinsiyeti == 'e':
        cinsiyeti = "ERKEK"
    else:
        cinsiyeti = "KADIN"
    print("-" * 50)
    print("Yazar İsmi: ", yazarAdi.upper())
    print("Cinsiyeti: ", cinsiyeti.upper())


def listele3(ad, cinsiyet):
    for i in range(len(ad)):
        liste3(ad[i], cinsiyet[i])


def encok(sayfa,ad,cinsiyet):
    ecs = sayfa[0]
    yazari = kitap[0]
    for i in range(len(ad)):
        if sayfa[i] > ecs:
            ecs = sayfa[i]
            yazari = ad[i]
            if cinsiyet[i] == 'e':
                cinsiyet = "ERKEK"
            else:
                cinsiyet = "KADIN"
    print("En Çok Sayfası olan kitap", ecs, "sayfa ile", yazari.upper(), "tarafından yazılmıstır ve cinsiyeti", cinsiyet, "dir" )


def enaz(sayfa, ad, cinsiyet):
    eas = sayfa[0]
    yazari = kitap[0]
    for i in range(len(ad)):
        if sayfa[i] < eas:
            eas = sayfa[i]
            yazari = ad[i]
            if cinsiyet[i] == 'e':
                cinsiyet = "ERKEK"
            else:
                cinsiyet = "KADIN"
    print("En Az Sayfası olan kitap", eas, "sayfa ile", yazari.upper(), "tarafından yazılmıstır ve cinsiyeti", cinsiyet, "dir")


def ErkekKadin(cinsiyet):
    toplame=0
    toplamk=0
    for i in range(len(cinsiyet)):
        if cinsiyet[i] =='e':
            toplame=toplame+1
        else:
            toplamk=toplamk+1
    print("toplam erkek yazar sayısı", toplame, "toplam kadın yazar sayısı", toplamk)
while tekrar == 'E':
    ad = ["ali", "veli", "hasan", "ayse", "fatma", "canan", "erhan"]
    kitap = ["matematik", "fizik", "geometri", "felsefe", "turkce", "tarih", "kimya"]
    sayfa = [500, 350, 450, 150, 340, 375, 700]
    cinsiyet = ["e", "e", "e", "k", "k", "k", "e"]


    # print(len(ad),len(kitap),len(sayfa),len(cinsiyet))
    # print(type(sayfa[1]))
    def menu():
        print(""" 
     1. Listele
     2. Yazarları kitapları ile birlikte listele
     3. Yazarları cinsiyetlerine göre listele 
     4. En çok sayfası olan kitabı göster
     5. En az sayfası olan kitabı listele
     6. En çok sayfası olan kitabın yazarının ismi ve cinsiyeti
     7. En az sayfası olan kitabın yazarı ve cinsiyeti
     8. Kaç erkek, kaç bayan yazar var
     9. Ortalama sayfa sayısı
     10. Çıkış
     """)


    menu()
    sec = int(input("Yapılacak işlemi Seçiniz"))
    if sec == 1:
        listele(ad, kitap, sayfa, cinsiyet)
    elif sec == 2:
        listele2(ad, kitap)
    elif sec == 3:
        listele3(ad, cinsiyet)
    elif sec == 4:
        ecs = sayfa[0]
        kitapecs = kitap[0]
        for i in range(len(ad)):
            if sayfa[i] > ecs:
                ecs = sayfa[i]
                kitapecs = kitap[i]
        print("En Çok Sayfası olan kitap", ecs, "sayfa ile", kitapecs.upper(), "İsimli Kitaptır")
    elif sec == 5:
        eas = sayfa[0]
        kitapeas = kitap[0]
        for i in range(len(ad)):
            if sayfa[i] < eas:
                eas = sayfa[i]
                kitapeas = kitap[i]
        print("En Az Sayfası olan kitap", eas, "ile", kitapeas.upper(), "İsimli Kitaptır")
    elif sec == 6:
        encok(sayfa,ad,cinsiyet)
    elif sec == 7:
        enaz(sayfa,ad,cinsiyet)
    elif sec == 8:
        ErkekKadin(cinsiyet)
    elif sec == 9:
        toplamsayfa=0
        i=0
        for i in range(len(ad)):
            toplamsayfa=toplamsayfa+sayfa[i]
            print(i)
            print(toplamsayfa)
        print("Kütüphanedeki kitapların ortalama sayfası ",(toplamsayfa/(i+1)), " kadardır.")
    elif sec == 10:
        exit(0)
    else:
        print("Yanlış seçim yaptınız")
    tekrar = str(input("Yeni İşlem Yapmak İstiyormusunuz (E/H)")).upper()
