# Döngüler ve Sorgular

#### if
hava_durumu = "yagisli"

if hava_durumu == 'yagisli':
    print("Semsiyeni Al!")

#### if - else  
hava_durumu = "günesli"

if hava_durumu == 'yagisli':
    print("Semsiyeni Al!")
else:
    print("Sapka Al!")

#### if elif else
hava_durumu = "karli"

if hava_durumu == 'yagisli':
    print("Semsiyeni Al!")
elif hava_durumu == 'karli':
    print("Atkini Al!")
else:
    print("Sorun yok")

####
yas = 35
if yas>18:
    print("Selam")
else:
    print("Sen buraya ait değilsin")

####
liste=['a','b','c']

hedef_harf = 'd'
if hedef_harf in liste:
    print("Buldum")
else:
    liste.append(hedef_harf)
    print("Guncel Liste {}".format(liste))

####
if (hedef_harf in liste) and (hedef_harf == liste[0]):
    print("Buldum ve ilk harf konumunda.")
elif hedef_harf in liste:
    print("Buldum ama ilk konumda değil.")
else:
    liste.append(hedef_harf)
    print("Listeye ekledim.")
    print("Guncel Liste {}".format(liste))

#### Listelerde for döngüsü
best_friends= ["Betül Badem","Elif Alış","Eren Çakıl","Şaziye Dağ","Zeynep Özdemir"]
for friend in best_friends:
    print(friend)

sayi=0
for friend in best_friends:
    sayi = sayi+1
    print(sayi,friend)

sayi=0
for friend in best_friends:
    sayi = sayi+1
    ad,soyad = friend.split()[0],friend.split()[1]
    print("{0}. Arkadasimin Adi {1} ve Soyadi {2}".format(sayi,ad,soyad))

Caliskan ="Betül Badem"
sayi=0
Caliskan_sayisi = 0

for friend in best_friends:
    ad,soyad = friend.split()[0],friend.split()[1]

    if(friend==Caliskan):
        Caliskan_sayisi+= 1
        print("{0}. Çalışkan Arkadasimin Adi {1} ve Soyadi {2}".format(Caliskan_sayisi,ad,soyad))

    else:
        sayi = sayi+1
        print("{0}. Arkadasimin Adi {1} ve Soyadi {2}".format(sayi,ad,soyad))

#### Diğer Iterable Objelerde for Döngüleri
tup1 = (1,3,5,7,)
for sayi in tup1:
    print(sayi)

liste = [[1,2],[3,4],[5,6],['a','b']]
for deger1,deger2 in liste:
    print(deger1)

liste = [[1,2],[3,4],[5,6]]
for x,y in liste:
    print(x,y)

liste = [[1,2],[3,4],[5,6]]
for x,y in liste:
    print(x*y)

#### dictionary
kullanici1= {
    'Ad': 'Büşra',
    'Soyad': 'Kaya'
}
print(kullanici1)

for k,v in kullanici1.items():
    print("Key: {} \t Value: {}".format(k,v))

for k in kullanici1.keys():
    print("Key: {}".format(k))

for v in kullanici1.values():
    print("Value: {}".format(v))

#### while döngüsü
x=0
while x<10:
    print("{} degeri 10'dan kücüktür.".format(x))
    x+=1

x=0
while x<10:
    print("{} degeri 10'dan kücüktür.".format(x))
    x+=1
else:
    print("{} degeri 10'dan kücük değil.".format(x))


#### while ile faktöriyel hesaplama

sayi = 6
faktoriyel=1
while sayi > 0:
    faktoriyel = faktoriyel*sayi
    sayi-= 1

print(faktoriyel)

#### range
print(range(10))
print(type(range(10)))

liste=[1,2,3]
print(liste)
print(type(liste))

print(list(range(10)))
print([*range(10)])

print([*range(2,7)])
print([*range(2,7,2)])

for sayi in range(10):
    print(sayi)

print("\n")
for sayi in range(10):
    if sayi>5:
        print(sayi)

print("\n")

#### enumerate 
harfler = ['a','b','c','d','e']
for harf in harfler:
    print(harf)

print("\n")
harfler = ['a','b','c','d','e']
for harf in enumerate(harfler):
    print(harf)

print("\n")
for index, harf in enumerate(harfler):
    print(index,harf)

print("\n")
for index, harf in enumerate(harfler):
    print(index+1,harf)

print("\n")
for index, harf in enumerate(harfler):
    print("{}.harf : {}".format(index+1,harf))

print("\n")

#### zip uzunlu eşit 2 listenin birleştirilmesi    
ulkeler=['TR','FR','DE']
siralamalar=range(1,4)

for ulke in zip(ulkeler,siralamalar):
    print(ulke)

print("\n")
for ulke,siralama in zip(ulkeler,siralamalar):
    print(ulke)

#### break
print("\n")
harfler = ['a','b','c','d','e']*100
for index,harf in enumerate(harfler):
    if harf =='c':
        print("{} harfi : {}.indexte!".format(harf,index))
        break

print("\n")
#### continue
for sayi in range(1,6):
    if sayi%2==0:
        continue
    print(sayi)

print("\n")
#### pass
for sayi in range(1,6):
    if sayi%2==0:
        pass
    else:
        print(sayi)

if sayi < 5:
    pass #oluşturulmamış kodlar yerine yazılır hata almamakiçin
else:
    print("hey")