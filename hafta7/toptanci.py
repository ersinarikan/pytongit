# 4 liste prinç mercimek fasulye nohut
mercimek = []
pirinc = []
fasulye = []
nohut = []


def listele(fasulye, nohut, mercimek, pirinc):
    i = 0
    toplamFasulye = 0
    j = 0
    toplamNohut = 0
    k = 0
    toplamPirinc = 0
    z = 0
    toplamMercimek = 0

    for i in range(len(fasulye)):
        toplamFasulye = fasulye[i] + toplamFasulye
    print(toplamFasulye, "depoda bulnan toplam fasulye miktarı")

    for j in range(len(nohut)):
        toplamNohut = nohut[j] + toplamNohut
    print(toplamNohut, "depoda bulnan toplam nohut miktarı")

    for k in range(len(pirinc)):
        toplamPirinc = pirinc[k] + toplamPirinc
    print(toplamPirinc, "depoda bulnan toplam pirinc miktarı")

    for z in range(len(mercimek)):
        toplamMercimek = mercimek[z] + toplamMercimek
    print(toplamNohut, "depoda bulnan toplam Mercimek miktarı")


while True:
    sec = int(input(""" 
              1. Depoya giriş
              2. Depodan çıkış
              3. listele """))
    if sec == 1:
        giris = int(input(""" 
                1. Mercimek
                2. Pirinç
                3. Nohut
                4. Fasulye"""))
        if giris == 1:
            giriskgMr = int(input("""
                1. 10 KG
                2. 50 KG
                3. 100 KG"""))
            if giriskgMr == 1:
                mercimek.append(10)
            if giriskgMr == 2:
                mercimek.append(50)
            if giriskgMr == 3:
                mercimek.append(100)
        if giris == 2:
            giriskgPr = int(input("""
            1. 10 KG
            2. 50 KG
            3. 100 KG"""))
            if giriskgPr == 1:
                pirinc.append(10)
            if giriskgPr == 2:
                pirinc.append(50)
            if giriskgPr == 3:
                pirinc.append(100)
        if giris == 3:
            giriskgNh = int(input("""
            1. 10 KG
            2. 50 KG
            3. 100 KG"""))
            if giriskgNh == 1:
                nohut.append(10)
            if giriskgNh == 2:
                nohut.append(50)
            if giriskgNh == 3:
                nohut.append(100)
        if giris == 4:
            giriskgFs = int(input("""
            1. 10 KG
            2. 50 KG
            3. 100 KG"""))
            if giriskgFs == 1:
                fasulye.append(10)
            if giriskgFs == 2:
                fasulye.append(50)
            if giriskgFs == 3:
                fasulye.append(100)
    # print(fasulye)
    # print(nohut)
    # print(pirinc)
    # print(mercimek)
    if sec == 2:
        giris = int(input(""" 
                   1. Mercimek
                   2. Pirinç
                   3. Nohut
                   4. Fasulye"""))
        if giris == 1:
            giriskgM = int(input("""
                   1. 10 KG
                   2. 50 KG
                   3. 100 KG"""))
            if giriskgM == 1:
                mercimek.remove(10)
            if giriskgM == 2:
                mercimek.remove(50)
            if giriskgM == 3:
                mercimek.remove(100)
        if giris == 2:
            giriskgP = int(input("""
               1. 10 KG
               2. 50 KG
               3. 100 KG"""))
            if giriskgP == 1:
                pirinc.remove(10)
            if giriskgP == 2:
                pirinc.remove(50)
            if giriskgP == 3:
                pirinc.remove(100)
        if giris == 3:
            giriskgN = int(input("""
               1. 10 KG
               2. 50 KG
               3. 100 KG"""))
            if giriskgN == 1:
                nohut.remove(10)
            if (giriskgN == 2):
                nohut.remove(50)
            if giriskgN == 3:
                nohut.remove(100)
        if giris == 4:
            giriskgF = int(input("""
               1. 10 KG
               2. 50 KG
               3. 100 KG"""))
            if giriskgF == 1:
                fasulye.remove(10)
            if giriskgF == 2:
                fasulye.remove(50)
            if giriskgF == 3:
                fasulye.remove(100)
    if sec == 3:
        listele(fasulye, nohut, mercimek, pirinc)
