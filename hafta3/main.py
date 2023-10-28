#faiz hesaplama
faturaTipi=(input("Fatura Tipini giriniz Gıda için (G), Elektronik için (E) "))
faturaTutari=0
fatura=0
if(faturaTipi=='E'):
    faturaTutari = int(input("Fatura Tutarını giriniz : "))
    fatura=(faturaTutari*118/100)
    print("Fatura Tutarı= : ",fatura," TL ")
elif(faturaTipi=='e'):
    faturaTutari = int(input("Fatura Tutarını giriniz : "))
    fatura=(faturaTutari*118/100)
    print("Fatura Tutarı= : ", fatura, " TL ")
elif(faturaTipi=='G'):
    faturaTutari = int(input("Fatura Tutarını giriniz : "))
    fatura=(faturaTutari*108/100)
    print("Fatura Tutarı= : ",fatura," TL ")
elif(faturaTipi=='g'):
    faturaTutari = int(input("Fatura Tutarını giriniz : "))
    fatura=(faturaTutari*108/100)
    print("Fatura Tutarı= : ",fatura," TL ")
else:
    print("Yanlış veri grişi")