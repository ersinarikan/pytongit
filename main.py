liste1=[]#boş liste oluşturma
liste2=list()
print(liste1,type(liste1))
print(liste2,type(liste2))
vNot=[10,5,6,8,3] #içine başlangıç değeri aktarılan liste oluşturma
print(vNot)
print(vNot[0])
print(vNot[3])
toplam=vNot[0]+vNot[1]+vNot[2]+vNot[3]+vNot[4]
listeElemanSayisi=len(vNot)
print(toplam/listeElemanSayisi)
print(vNot[-1])
print(vNot[::-1])
print(vNot[1:3])
#listenin ilk elemanı
print(vNot[0])
#listenin son elemanı
print(vNot[-1])
print(vNot[len(vNot)-1])
print(vNot[:4])
print(vNot[2:])
print(vNot[::2])
print(vNot[::-1])
l1=[1,3,5]
l2=[2,4,6,8]
l3=l1+l2
print("l1 ",l1)
print("l2 ",l2)
print("l3 ",l3)
l1=l1+["Nurşen"]
print(l1)
l1=l1+[10,20]#listeye eleman ekleme
print(l1)
print(l2*2)
print(l2)
l2.append(50)#sadece tek değer eklenir
print(l2)
l2.append(["a","b","c"])
print(l2)
print(l2[5])
print(l2[5][1])
popIslem=l2.pop() #listenin son elemanını listeden çıkarır
print("popIslem",popIslem)
print("l2",l2)
silme2=l2.pop(2)#belirtilen indis değerini listeden siler
print("silme2",silme2)
print(l2)
print(l1)
liste1=[54,21,6,87,23,98,34]
liste1.sort()
print(liste1)
liste1.sort(reverse=True)
print(liste1)
ad=["ayşe","mehmet","zeynep","ahmet","nurten","Zeynep","Zeliha"]
ad.sort()
print(ad)
ad.sort(reverse=True)
print(ad)
li1=[1,2]
li2=[10,20]
li3=[100,200]
li4=li1+li2+li3
print(li4)
li5=[li1,li2,li3]
print(li5)
print(li5[0])
print(li5[1])
print(li5[2])
print(li5[2][0])
li5[2][0]=500
print(li5[2])



