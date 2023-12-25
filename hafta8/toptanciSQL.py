from hafta8 import toptancisqlfonk

db = toptancisqlfonk.sql()
db.create()
while True:
    sec = int(input(""" 
              1. Depoya giris
              2. Depodan cikis
              3. Raporlar 
              4. Çıkış"""))
    if sec == 1:
        giris = int(input(""" 
                1. Mercimek
                2. Pirinc
                3. Nohut
                4. Fasulye"""))
        if giris == 1:
            giriskgMr = int(input("""
                1. 10 KG
                2. 50 KG
                3. 100 KG"""))
            if giriskgMr == 1:
                bakliyat_ismi = "Mercimek"
                kg = 10
                depo_numarasi = int(input("Depo Numarasını giriniz 1/2: "))
                adet = int(input("Kaç Adet : "))
                db.ekle(bakliyat_ismi, depo_numarasi, adet, kg)

            elif giriskgMr == 2:
                bakliyat_ismi = "Mercimek"
                kg = 50
                depo_numarasi = int(input("Depo Numarasını giriniz 1/2: "))
                adet = int(input("Kaç Adet : "))
                db.ekle(bakliyat_ismi, depo_numarasi, adet, kg)
            elif giriskgMr == 3:
                bakliyat_ismi = "Mercimek"
                kg = 100
                depo_numarasi = int(input("Depo Numarasını giriniz 1/2: "))
                adet = int(input("Kaç Adet : "))
                db.ekle(bakliyat_ismi, depo_numarasi, adet, kg)
            else:
                print("Yanlış seçim yaptınız")

        elif giris == 2:
            giriskgPr = int(input("""
            1. 10 KG
            2. 50 KG
            3. 100 KG"""))
            if giriskgPr == 1:
                bakliyat_ismi = "Pirinç"
                kg = 10
                depo_numarasi = int(input("Depo Numarasını giriniz 1/2: "))
                adet = int(input("Kaç Adet : "))
                db.ekle(bakliyat_ismi, depo_numarasi, adet, kg)
            elif giriskgPr == 2:
                bakliyat_ismi = "Pirinç"
                kg = 50
                depo_numarasi = int(input("Depo Numarasını giriniz 1/2: "))
                adet = int(input("Kaç Adet : "))
                db.ekle(bakliyat_ismi, depo_numarasi, adet, kg)
            elif giriskgPr == 3:
                bakliyat_ismi = "Pirinç"
                kg = 100
                depo_numarasi = int(input("Depo Numarasını giriniz 1/2: "))
                adet = int(input("Kaç Adet : "))
                db.ekle(bakliyat_ismi, depo_numarasi, adet, kg)
            else:
                print("Yanlış seçim yaptınız")
        elif giris == 3:
            giriskgNh = int(input("""
            1. 10 KG
            2. 50 KG
            3. 100 KG"""))
            if giriskgNh == 1:
                bakliyat_ismi = "Nohut"
                kg = 10
                depo_numarasi = int(input("Depo Numarasını giriniz 1/2: "))
                adet = int(input("Kaç Adet : "))
                db.ekle(bakliyat_ismi, depo_numarasi, adet, kg)
            elif giriskgNh == 2:
                bakliyat_ismi = "Nohut"
                kg = 50
                depo_numarasi = int(input("Depo Numarasını giriniz 1/2: "))
                adet = int(input("Kaç Adet : "))
                db.ekle(bakliyat_ismi, depo_numarasi, adet, kg)
            elif giriskgNh == 3:
                bakliyat_ismi = "Nohut"
                kg = 100
                depo_numarasi = int(input("Depo Numarasını giriniz 1/2: "))
                adet = int(input("Kaç Adet : "))
                db.ekle(bakliyat_ismi, depo_numarasi, adet, kg)
            else:
                print("Yanlış seçim yaptınız")
        elif giris == 4:
            giriskgFs = int(input("""
            1. 10 KG
            2. 50 KG
            3. 100 KG"""))
            if giriskgFs == 1:
                bakliyat_ismi = "Fasulye"
                kg = 10
                depo_numarasi = int(input("Depo Numarasını giriniz 1/2: "))
                adet = int(input("Kaç Adet : "))
                db.ekle(bakliyat_ismi, depo_numarasi, adet, kg)
            elif giriskgFs == 2:
                bakliyat_ismi = "Fasulye"
                kg = 50
                depo_numarasi = int(input("Depo Numarasını giriniz 1/2: "))
                adet = int(input("Kaç Adet : "))
                db.ekle(bakliyat_ismi, depo_numarasi, adet, kg)
            elif giriskgFs == 3:
                bakliyat_ismi = "Fasulye"
                kg = 100
                depo_numarasi = int(input("Depo Numarasını giriniz 1/2: "))
                adet = int(input("Kaç Adet : "))
                db.ekle(bakliyat_ismi, depo_numarasi, adet, kg)
            else:
                print("Yanlış seçim yaptınız")
        else:
            print("Yanlış işlem seçtiniz")
    elif sec == 2:
        giris = int(input(""" 
                   1. Mercimek
                   2. Pirinc
                   3. Nohut
                   4. Fasulye"""))
        if giris == 1:
            giriskgM = int(input("""
                   1. 10 KG
                   2. 50 KG
                   3. 100 KG"""))
            if giriskgM == 1:
                bakliyat_ismi = "Mercimek"
                kg = -10
                depo_numarasi = int(input("Depo Numarasını giriniz 1/2: "))
                adet = int(input("Kaç Adet : "))
                db.ekle(bakliyat_ismi, depo_numarasi, adet, kg)
            elif giriskgM == 2:
                bakliyat_ismi = "Mercimek"
                kg = -50
                depo_numarasi = int(input("Depo Numarasını giriniz 1/2: "))
                adet = int(input("Kaç Adet : "))
                db.ekle(bakliyat_ismi, depo_numarasi, adet, kg)
            elif giriskgM == 3:
                bakliyat_ismi = "Mercimek"
                kg = -100
                depo_numarasi = int(input("Depo Numarasını giriniz 1/2: "))
                adet = int(input("Kaç Adet : "))
                db.ekle(bakliyat_ismi, depo_numarasi, adet, kg)
            else:
                print("Yanlış seçim yaptınız")
        if giris == 2:
            giriskgP = int(input("""
               1. 10 KG
               2. 50 KG
               3. 100 KG"""))
            if giriskgP == 1:
                bakliyat_ismi = "Pirinç"
                kg = -10
                depo_numarasi = int(input("Depo Numarasını giriniz 1/2: "))
                adet = int(input("Kaç Adet : "))
                db.ekle(bakliyat_ismi, depo_numarasi, adet, kg)
            elif giriskgP == 2:
                bakliyat_ismi = "Pirinç"
                kg = -50
                depo_numarasi = int(input("Depo Numarasını giriniz 1/2: "))
                adet = int(input("Kaç Adet : "))
                db.ekle(bakliyat_ismi, depo_numarasi, adet, kg)
            elif giriskgP == 3:
                bakliyat_ismi = "Pirinç"
                kg = -100
                depo_numarasi = int(input("Depo Numarasını giriniz 1/2: "))
                adet = int(input("Kaç Adet : "))
                db.ekle(bakliyat_ismi, depo_numarasi, adet, kg)
            else:
                print("Yanlış seçim yaptınız")
        if giris == 3:
            giriskgN = int(input("""
               1. 10 KG
               2. 50 KG
               3. 100 KG"""))
            if giriskgN == 1:
                bakliyat_ismi = "Nohut"
                kg = -10
                depo_numarasi = int(input("Depo Numarasını giriniz 1/2: "))
                adet = int(input("Kaç Adet : "))
                db.ekle(bakliyat_ismi, depo_numarasi, adet, kg)
            elif (giriskgN == 2):
                bakliyat_ismi = "Nohut"
                kg = -50
                depo_numarasi = int(input("Depo Numarasını giriniz 1/2: "))
                adet = int(input("Kaç Adet : "))
                db.ekle(bakliyat_ismi, depo_numarasi, adet, kg)
            elif giriskgN == 3:
                bakliyat_ismi = "Nohut"
                kg = -100
                depo_numarasi = int(input("Depo Numarasını giriniz 1/2: "))
                adet = int(input("Kaç Adet : "))
                db.ekle(bakliyat_ismi, depo_numarasi, adet, kg)
            else:
                print("Yanlış seçim yaptınız")
        if giris == 4:
            giriskgF = int(input("""
               1. 10 KG
               2. 50 KG
               3. 100 KG"""))
            if giriskgF == 1:
                bakliyat_ismi = "Fasulye"
                kg = -10
                depo_numarasi = int(input("Depo Numarasını giriniz 1/2: "))
                adet = int(input("Kaç Adet : "))
                db.ekle(bakliyat_ismi, depo_numarasi, adet, kg)
            elif giriskgF == 2:
                bakliyat_ismi = "Fasulye"
                kg = -50
                depo_numarasi = int(input("Depo Numarasını giriniz 1/2: "))
                adet = int(input("Kaç Adet : "))
                db.ekle(bakliyat_ismi, depo_numarasi, adet, kg)
            elif giriskgF == 3:
                bakliyat_ismi = "Fasulye"
                kg = -100
                depo_numarasi = int(input("Depo Numarasını giriniz 1/2: "))
                adet = int(input("Kaç Adet : "))
                db.ekle(bakliyat_ismi, depo_numarasi, adet, kg)
            else:
                print("Yanlış seçim yaptınız")
    elif sec == 3:
        rapor = int(input("""
           1. Depolara Göre Rapor
           2. Bakliyat Raporu
           3. Çıkış"""))
        if rapor == 1:
            toptancisqlfonk.sql.rapor1()

        elif rapor == 2:
            pass  # tüm depolarda ne kadar ürün olduğunu göster

        else:
            print("Yanlış Seçim Yaptınız")
    elif sec == 4:
        print("Programdan çıkılıyor")
        exit(0)
    else:
        print("Yanlış İşlem Seçimi")
