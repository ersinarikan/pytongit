class Araba:
    def __init__(self, marka, model, renk, uretimYili, saseNo):
        self.marka = marka
        self.model = model
        self.renk = renk
        self.uretimYili = uretimYili
        self.saseNo = saseNo
class Opsiyonlar(Araba):
    def __init__(self, marka, model, renk, uretimYili, saseNo, kullanimAmaci, fiyati):
        super().__init__(marka, model, renk, uretimYili, saseNo)
        self.kullanimAmaci = kullanimAmaci
        self.fiyati = fiyati
    def __str__(self):
        return f"Marka:{self.marka}, Model:{self.model}, Renk:{self.renk}, UretimYili:{self.uretimYili}, SaseNo:{self.saseNo}, KullanimAmaci:{self.kullanimAmaci}, Fiyati:{self.fiyati}"


arabalar=[]
def kayitGirisi():
    marka = input("Aracin Markasini Giriniz :")
    model = input("Aracin Modelini Giriniz :")
    renk = input("Aracin Rengini Giriniz :")
    uretimYili = int(input("Aracin Uretim Yilini Giriniz: "))
    saseNo = int(input("Aracin Sase numarasini Giriniz :"))
    kullanimAmaci = input("Aracin Kullanim Amacini Giriniz :")
    fiyati = int(input("Aracin Fiyatini Giriniz :"))
    yeniOpsiyon = Opsiyonlar(marka, model, renk, uretimYili, saseNo, kullanimAmaci, fiyati)
    arabalar.append(yeniOpsiyon)


def kayitListele():
    for Opsiyonlar in arabalar:
        print("-"*75)
        print("Markasi : ", Opsiyonlar.marka)
        print("Modeli : ", Opsiyonlar.model)
        print("Rengi : ", Opsiyonlar.renk)
        print("Uretim Yılı : ", Opsiyonlar.uretimYili)
        print("Kullanım Amaci : ", Opsiyonlar.kullanimAmaci)
        print("Fiyati : ", Opsiyonlar.fiyati)
        print("-" * 75)
def kayitDuzelt():
    kayitDuzeltilecekSase = int(input("Kayit duzeltilecek Sase numarasini Giriniz: "))
    for Opsiyonlar in arabalar:
        if kayitDuzeltilecekSase == Opsiyonlar.saseNo:
            print("Mevcut Bilgiler:")
            print("Markasi : ", Opsiyonlar.marka)
            print("Modeli : ", Opsiyonlar.model)
            print("Rengi : ", Opsiyonlar.renk)
            print("Uretim Yılı : ", Opsiyonlar.uretimYili)
            print("Kullanım Amaci : ", Opsiyonlar.kullanimAmaci)
            print("Fiyati : ", Opsiyonlar.fiyati)

            Opsiyonlar.marka = input("Yeni Marka: ")
            Opsiyonlar.model = input("Yeni Model: ")
            Opsiyonlar.renk = input("Yeni Renk: ")
            Opsiyonlar.uretimYili = int(input("Yeni Uretim Yili: "))
            Opsiyonlar.kullanimAmaci = input("Yeni Kullanım Amaci: ")
            Opsiyonlar.fiyati = int(input("Yeni Fiyat: "))

            print("Kayıt başarıyla güncellendi.")
            return  # işlem tamamlandı, fonksiyondan çık

    print("Belirtilen şase numarasına sahip araç bulunamadı.")
def istatistikGoster():
    enYuksekFiyatliArac = 0
    enKucukFiyatliArac = 250000000
    enGencArac = 0
    enYasliArac = 3000
    ate = 0
    for Opsiyonlar in arabalar:
        ate=Opsiyonlar.fiyati+ate

        if Opsiyonlar.fiyati > enYuksekFiyatliArac:
            enYuksekFiyatliArac = Opsiyonlar.fiyati
            enYuksekFiyatliAracMarkasi=Opsiyonlar.marka
            enYuksekFiyatliAracModeli = Opsiyonlar.model

        if Opsiyonlar.fiyati < enKucukFiyatliArac:
            enKucukFiyatliArac = Opsiyonlar.fiyati
            enKucukFiyatliAracMarkasi=Opsiyonlar.marka
            enKucukFiyatliAracModeli = Opsiyonlar.model

        if Opsiyonlar.uretimYili > enGencArac:
            enGencArac = Opsiyonlar.uretimYili
            enGencAracMarkasi = Opsiyonlar.marka
            enGencracModeli = Opsiyonlar.model

        if Opsiyonlar.uretimYili < enYasliArac:
            enYasliArac = Opsiyonlar.uretimYili
            enYasliAracMarkasi = Opsiyonlar.marka
            enYasliaracModeli = Opsiyonlar.model

    print(f"En Yüksek Fiyatlı Araç: {enYuksekFiyatliArac} Markası: {enYuksekFiyatliAracMarkasi} Modeli: {enYuksekFiyatliAracModeli}")
    print(f"En Düşük Fiyatlı Araç: {enKucukFiyatliArac} Markası: {enKucukFiyatliAracMarkasi} Modeli: {enKucukFiyatliAracModeli}")
    print(f"En Genç Arac: {enGencArac} Markası: {enGencAracMarkasi} Modeli: {enGencracModeli}")
    print(f"En Yaşlı Arac: {enYasliArac} Markası: {enYasliAracMarkasi} Modeli: {enYasliaracModeli}")
    print(f"Aracların Toplam Ederi: {ate} ")
    print(f"Aracların Ortalama Ederi: {ate/len(arabalar)} ")


def kayitSilme():
    kayitSilinecekSase = int(input("Kayit Silinecek Sase numarasini Giriniz: "))
    found = False
    for Opsiyonlar in arabalar:
        if kayitSilinecekSase == Opsiyonlar.saseNo:
            print("Silinen Kayıt Bilgileri:")
            print("-" * 75)
            print("Markasi : ", Opsiyonlar.marka)
            print("Modeli : ", Opsiyonlar.model)
            print("Rengi : ", Opsiyonlar.renk)
            print("Uretim Yılı : ", Opsiyonlar.uretimYili)
            print("Kullanım Amaci : ", Opsiyonlar.kullanimAmaci)
            print("Fiyati : ", Opsiyonlar.fiyati)
            print("-" * 75)

            arabalar.remove(Opsiyonlar)
            found = True
            print("Kayıt başarıyla silindi.")
            break
    if not found:
        print("Belirtilen şase numarasına sahip araç bulunamadı.")


while True:
    print("""
    1. Kayit Girişi
    2. Kayitlari Listele
    3. Kayit Duzelt
    4. Kayit Silme
    5. Istatistikleri Goster
    6. Cikis""")
    secim = int(input("Secimizi Yapınız"))
    if secim == 1:
        kayitGirisi()
    elif secim == 2:
        kayitListele()
    elif secim == 3:
        kayitDuzelt()
    elif secim == 4:
        kayitSilme()
    elif secim == 5:
        istatistikGoster()
    elif secim == 6:
        exit(0)
    else:
        print("Yanlış Seçim Yaptınız")

