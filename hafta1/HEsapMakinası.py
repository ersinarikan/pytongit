s1=int(input("Birinci sayı"))
s2=int(input("İkinci sayı"))
islem=input("""+-Toplama
- - Çıkarma
* - Çarpma
/ - Bölme""")
if islem=="+":
    print(s1,"+",s2,"=",(s1+s2))
elif islem=="-":
    print(s1,"-",s2,"=",(s1-s2))
elif islem=="*":
    print(s1,"*",s2,"=",(s1*s2))
elif islem=="/":
    print(s1,"/",s2,"=",(s1/s2))
else:
    print("yanlış işlem seçimi")

