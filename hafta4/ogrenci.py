ad=list()
vn=[]
fn=[]
bn=[]
kisi=int(input("Kişi sayısını giriniz :"))
for i in range(kisi):
    ad.append(input("isim giriniz"))
    vnGecici=(input("vize notu giriniz :"))
    vn.append(vnGecici)
    fnGecici=int(input("Final notunu girinmiz:"))
    fn.append(fnGecici)
    bn.append((vnGecici*0.4+fnGecici*0.6))
print("isimler:" ,ad)
print("vize",vn)
print("final",fn)
print("başarı",bn)

