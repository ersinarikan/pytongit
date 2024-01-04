from hafta8 import toptancisqlfonk

db = toptancisqlfonk.sql()
db.create()


def girisler(bakliyat_ismi, kg):
    depo_numarasi = int(input(f"{kg} lık {bakliyat_ismi} Ürünü Kac Numaralı Depoya Girecek Secin 1/2: "))
    adet = int(input(f"{depo_numarasi} Numarali Depoya Kac Cuval {bakliyat_ismi} Girisi Yapilacak: "))
    if depo_numarasi == 1 or depo_numarasi == 2:
        pass
    else:
        print("Lutfen Tanimli Bir Depo Numarası Secin 1 veya 2")
    db.ekle(bakliyat_ismi, depo_numarasi, adet, kg)
    print("Tebrikler", depo_numarasi, " Numarali Depoya", adet, " Cuval", kg, " KG'lık", bakliyat_ismi,
          " Girisi Yapilmistir.")


def cikislar(bakliyat_ismi, kg):
    depo_numarasi = int(input(f"{-kg} lık {bakliyat_ismi} Ürünü Kac Numaralı Depodan Cikacak Secin 1/2: "))
    adet = int(input(f"{depo_numarasi} Numarali Depoda Kac Cuval {bakliyat_ismi} Cikis Yapilacak: "))
    if depo_numarasi == 1 or depo_numarasi == 2:
        pass
    else:
        print("Lutfen Tanimli Bir Depo Numarası Secin 1 veya 2")
    kutu1 = db.kontrol(bakliyat_ismi, depo_numarasi, -kg)
    print("Cuval sayisi", kutu1[0])
    print("Depo Numarasi", depo_numarasi)
    print("KG", kg)
    if kutu1[0] < adet or kutu1 == "None" :
        print(depo_numarasi, "Numaralı depoda yeteri kadar ürün yok")
    else:
        db.ekle(bakliyat_ismi, depo_numarasi, -adet, kg)


while True:
    sec = int(input("""
    Yapmak Istediginiz Islemi Seciniz. 
    1. Depoya Urun Girisi
    2. Depodan Urun Cikisi
    3. Depo Raprolari
    4. Programdan Çıkış"""))
    if sec == 1:
        giris = int(input("""
        Depoya Giris Yapmak Istediniz Urunu Seciniz. 
        1. Mercimek Girisi
        2. Pirinc Girisi
        3. Nohut Girisi
        4. Fasulye Girisi"""))
        if giris == 1:
            giriskgMr = int(input("""
            1. 10 KG'lık Cuval Girişi
            2. 50 KG'lık Cuval Girisi
            3. 100 KG'lık Cuval Girisi"""))
            if giriskgMr == 1:
                bakliyat_ismi = "Mercimek"
                kg = 10
                girisler(bakliyat_ismi, kg)
            elif giriskgMr == 2:
                bakliyat_ismi = "Mercimek"
                kg = 50
                girisler(bakliyat_ismi, kg)
            elif giriskgMr == 3:
                bakliyat_ismi = "Mercimek"
                kg = 100
                girisler(bakliyat_ismi, kg)
            else:
                print("Yanlış seçim yaptınız")

        elif giris == 2:
            giriskgPr = int(input("""
            1. 10 KG'lık Cuval Girişi
            2. 50 KG'lık Cuval Girisi
            3. 100 KG'lık Cuval Girisi"""))
            if giriskgPr == 1:
                bakliyat_ismi = "Pirinc"
                kg = 10
                girisler(bakliyat_ismi, kg)
            elif giriskgPr == 2:
                bakliyat_ismi = "Pirinc"
                kg = 50
                girisler(bakliyat_ismi, kg)
            elif giriskgPr == 3:
                bakliyat_ismi = "Pirinc"
                kg = 100
                girisler(bakliyat_ismi, kg)
            else:
                print("Yanlış seçim yaptınız")
        elif giris == 3:
            giriskgNh = int(input("""
            1. 10 KG'lık Cuval Girişi
            2. 50 KG'lık Cuval Girisi
            3. 100 KG'lık Cuval Girisi"""))
            if giriskgNh == 1:
                bakliyat_ismi = "Nohut"
                kg = 10
                girisler(bakliyat_ismi, kg)
            elif giriskgNh == 2:
                bakliyat_ismi = "Nohut"
                kg = 50
                girisler(bakliyat_ismi, kg)
            elif giriskgNh == 3:
                bakliyat_ismi = "Nohut"
                kg = 100
                girisler(bakliyat_ismi, kg)
            else:
                print("Yanlış seçim yaptınız")
        elif giris == 4:
            giriskgFs = int(input("""
            1. 10 KG'lık Cuval Girişi
            2. 50 KG'lık Cuval Girisi
            3. 100 KG'lık Cuval Girisi"""))
            if giriskgFs == 1:
                bakliyat_ismi = "Fasulye"
                kg = 10
                girisler(bakliyat_ismi, kg)
            elif giriskgFs == 2:
                bakliyat_ismi = "Fasulye"
                kg = 50
                girisler(bakliyat_ismi, kg)
            elif giriskgFs == 3:
                bakliyat_ismi = "Fasulye"
                kg = 100
                girisler(bakliyat_ismi, kg)
            else:
                print("Yanlış seçim yaptınız")
        else:
            print("Yanlış işlem seçtiniz")
    elif sec == 2:
        giris = int(input(""" 
    Depodan Cikis Yapmak Istediniz Urunu Seciniz. 
    1. Mercimek Cikisi
    2. Pirinc Cikisi
    3. Nohut Cikisi
    4. Fasulye Cikisi"""))
        if giris == 1:
            giriskgM = int(input("""
            1. 10 KG'lık Cuval Cikisi
            2. 50 KG'lık Cuval Cikisi
            3. 100 KG'lık Cuval Cikisi"""))
            if giriskgM == 1:
                bakliyat_ismi = "Mercimek"
                kg = -10
                cikislar(bakliyat_ismi, kg)

            elif giriskgM == 2:
                bakliyat_ismi = "Mercimek"
                kg = -50
                cikislar(bakliyat_ismi, kg)
            elif giriskgM == 3:
                bakliyat_ismi = "Mercimek"
                kg = -100
                cikislar(bakliyat_ismi, kg)
            else:
                print("Yanlış seçim yaptınız")
        if giris == 2:
            giriskgP = int(input("""
            1. 10 KG'lık Cuval Cikisi
            2. 50 KG'lık Cuval Cikisi
            3. 100 KG'lık Cuval Cikisi"""))
            if giriskgP == 1:
                bakliyat_ismi = "Pirinc"
                kg = -10
                cikislar(bakliyat_ismi, kg)
            elif giriskgP == 2:
                bakliyat_ismi = "Pirinc"
                kg = -50
                cikislar(bakliyat_ismi, kg)
            elif giriskgP == 3:
                bakliyat_ismi = "Pirinc"
                kg = -100
                cikislar(bakliyat_ismi, kg)
            else:
                print("Yanlış seçim yaptınız")
        if giris == 3:
            giriskgN = int(input("""
            1. 10 KG'lık Cuval Cikisi
            2. 50 KG'lık Cuval Cikisi
            3. 100 KG'lık Cuval Cikisi"""))
            if giriskgN == 1:
                bakliyat_ismi = "Nohut"
                kg = -10
                cikislar(bakliyat_ismi, kg)
            elif giriskgN == 2:
                bakliyat_ismi = "Nohut"
                kg = -50
                cikislar(bakliyat_ismi, kg)
            elif giriskgN == 3:
                bakliyat_ismi = "Nohut"
                kg = -100
                cikislar(bakliyat_ismi, kg)
            else:
                print("Yanlış seçim yaptınız")
        if giris == 4:
            giriskgF = int(input("""
            1. 10 KG'lık Cuval Cikisi
            2. 50 KG'lık Cuval Cikisi
            3. 100 KG'lık Cuval Cikisi"""))
            if giriskgF == 1:
                bakliyat_ismi = "Fasulye"
                kg = -10
                cikislar(bakliyat_ismi, kg)
            elif giriskgF == 2:
                bakliyat_ismi = "Fasulye"
                kg = -50
                cikislar(bakliyat_ismi, kg)
            elif giriskgF == 3:
                bakliyat_ismi = "Fasulye"
                kg = -100
                cikislar(bakliyat_ismi, kg)
            else:
                print("Yanlış seçim yaptınız")
    elif sec == 3:
        rapor = int(input("""
            1. Toplam Depo Raporu
            2. Bakliyat Raporu
            3. Çıkış"""))
        if rapor == 1:
            db.rapor1()
        elif rapor == 2:
            db.rapor2()

        else:
            print("Yanlış Seçim Yaptınız")
    elif sec == 4:
        print("Programdan çıkılıyor")
        exit(0)
    else:
        print("Yanlış İşlem Seçimi")
