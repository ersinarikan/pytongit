tekrar = 'E'

while tekrar == 'E':
    faturaSms = 0.0
    faturaKonusma = 0.0
    faturaInternet = 0.0
    fatura = 0.0
    otv = 0
    smsKullanimi = 0
    konusmaKullanimi = 0
    internetKullanimi = 0
    kampanyaSmsTipi = 0
    kampanyaKonusmaTipi = 0
    kampanyaInternetTipi = 0
    kampanyaSms = 'E'
    kampanyaKonusma = 'E'
    kampanyaInternet = 'E'
    print("FATURA HESAPLAMA UYGULAMASINA HOŞGELDİNİZ")
    telefonNumarasi = int(input("\n Telefon numarasını başında 0 olmadan ve boşluk kullanmadan Giriniz"))

    kampanyaSms = str(input(telefonNumarasi, " Numaralı Telefona Tanımlı Bır SMS Paketi Varmı (E/H)")).upper()
    if kampanyaSms == 'E':
        kampanyaSmsTipi = int(input(""" Lütfen SMS Paketini Seciniz 
        1. 100  SMS Bizden
        2. 500  SMS Bizden
        3. 1000 SMS Bizden."""))
    kampanyaKonusma = str(
        input(telefonNumarasi, " Numaralı Telefona Tanımlı Bır Konuşma Paketi Varmı (E/H)")).upper()
    if kampanyaKonusma == 'E':
        kampanyaKonusmaTipi = int(input(""" Lütfen Konuşma Paketini Seciniz 
        1. 1000 dk Bizden
        2. 2000 dk Bizden
        3. 3000 dk Bizden."""))
    kampanyaInternet = str(
        input(print(telefonNumarasi, " Numaralı Telefona Tanımlı Bır Internet Paketi Varmı (E/H)"))).upper()
    if kampanyaInternet == 'E':
        kampanyaInternetTipi = int(input(print(""" Lütfen İnternet Paketini Seciniz 
         1. 1  GB Bizden
         2. 5  GB Bizden
         3. 10 GB Bizden.""")))
    smsKullanimi = int(
        input(telefonNumarasi, "Fatura dönemi içerisinde kullanılan SMS miktarını giriniz.(adet)"))
    konusmaKullanimi = int(
        input(telefonNumarasi, "Fatura dönemi içerisinde kullanılan Konuşma miktarını giriniz.(dk)"))
    internetKullanimi = int(
        input(telefonNumarasi, "Fatura dönemi içerisinde kullanılan Internet miktarını giriniz.(MB)"))

    # SMS Hesaplama
    if kampanyaSmsTipi == 1:

        if smsKullanimi >= 100:
            faturaSms = float(((smsKullanimi - 100) * 1.5) + 50)
        else:
            faturaSms = 50

    elif kampanyaSmsTipi == 2:

        if smsKullanimi >= 500:
            faturaSms = float(((smsKullanimi - 500) * 1.5) + 60)
        else:
            faturaSms = 60

    elif kampanyaSmsTipi == 3:

        if smsKullanimi >= 1000:
            faturaSms = float(((smsKullanimi - 1000) * 1.5) + 70)
        else:
            faturaSms = 70

    else:
        faturaSms = float(smsKullanimi * 1.5)

    # Konuşma Hesaplama
    if kampanyaKonusmaTipi == 1:
        if konusmaKullanimi >= 1000:
            faturaKonusma = float(((konusmaKullanimi - 1000) * 1.5) + 50)
        else:
            faturaKonusma = 50

    elif kampanyaKonusmaTipi == 2:
        if konusmaKullanimi >= 2000:
            faturaKonusma = float(((konusmaKullanimi - 2000) * 1.5) + 60)
        else:
            faturaKonusma = 60
    elif kampanyaKonusmaTipi == 3:
        if konusmaKullanimi >= 3000:
            faturaKonusma = float(((konusmaKullanimi - 3000) * 1.5) + 70)
        else:
            faturaKonusma = 70
    else:
        faturaKonusma = float(konusmaKullanimi * 1.5)

    # Internet Hesaplama
    if kampanyaInternetTipi == 1:
        if internetKullanimi >= 1000:
            faturaInternet = float(((internetKullanimi - 1000) * 1.5) + 50)
        else:
            faturaInternet = 50
    elif kampanyaInternetTipi == 2:
        if internetKullanimi >= 5000:
            faturaInternet = float(((internetKullanimi - 5000) * 1.5) + 60)
        else:
            faturaInternet = 60

    elif kampanyaInternetTipi == 3:
        if internetKullanimi >= 10000:
            faturaInternet = float(((internetKullanimi - 10000) * 1.5) + 70)
        else:
            faturaInternet = 70
    else:
        faturaInternet = float(internetKullanimi * 1.5)
    print(faturaInternet, "\n", faturaKonusma, "\n", faturaSms, "\n")
    fatura = float(faturaInternet + faturaKonusma + faturaSms)
    otv = int(input("OTV oranını giriniz (%)"))
    toplamFatura = int(fatura * ((otv + 100) / 100))
    print(telefonNumarasi, "Numaralı Telefona Ait Fatura = ", toplamFatura, " TL dir")
    tekrar = str(input("Yeni Fatura Hesaplamak İstiyormusunuz (E/H)")).upper()
