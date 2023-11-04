# i=0
# while i<4:
#     print(i)
#     i=i+1
#
# i=0
# while True:
#     print(i)
#     i+=1
#     if i==4:
#         break
while True:
    s1=int(input("Birinci sayı"))
    s2=int(input("İkinci sayı"))
#while True:
    menu=int(input("""
    1-Toplam
    2-Çıkarma
    3-Çarpma
    4-Bölme
    5-Çıkış"""))
    if menu==1:
        print("{0} + {1} = {2}".format(s1,s2,(s1+s2)))
    elif menu==2:
        print("{0} - {1} = {2}".format(s1,s2,(s1-s2)))
    elif menu==3:
        print("{0} * {1} = {2}".format(s1,s2,(s1*s2)))
    elif menu==4:
        print("{0} / {1} = {2}".format(s1,s2,(s1/s2)))
    elif menu==5:
        break
    else:
        print("yanlış menü değeri")

print("bitti")

