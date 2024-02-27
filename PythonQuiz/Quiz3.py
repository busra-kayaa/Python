## Fonksiyon Uygulamasi

### Bilgi:
# 3 üzeri 2 = 9 
# Python'da üstel sayilari hesaplamak icin 3**2 seklinde gösterilir. 

#### Soru 1: Asagidaki fonskiyonu 2 parametre alacak ve üstel sonucu return edecek bicimde doldurun
def ustel_sayi_v1(taban,kuvvet):
    return taban**kuvvet
    
taban= input("Taban degeri giriniz:")
kuvvet = input("Üs degeri giriniz:")

sonuc=ustel_sayi_v1(int(taban),int(kuvvet))
print(sonuc)


#### Soru 2: Asagidaki fonskiyonu 2 parametre alacak ve üstel sonucu return edecek bicimde  ve  ** yerine for döngüsü ile hesaplayacak bicimde olusturun
def ustel_sayi_v2(taban,kuvvet):
    carpim = 1
    if kuvvet < 1:
        return carpim
    else:
        for kuvvet in range(1,kuvvet+1):
            carpim = carpim * taban
        return carpim

taban = input("Taban degeri giriniz:")
kuvvet = input("Üs degeri giriniz:")

sonuc2=ustel_sayi_v2(int(taban),int(kuvvet))
print(sonuc2)

### Bilgi:
# .sort() komutu listeyi kücükten büyüge siralar

#### Soru 3: Asagidaki fonskiyonu 1 parametre alacak (sadece sayilardan olusan liste tipinde) ve en büyük iki sayiyi döndürecek bicimde olusturun

sayilar = [1,9,8,3,4,2]
sayilar.sort()
print(sayilar)

def listedeki_en_buyuk_iki_sayi(list):
    list.sort()
    return list[-1],list[-2]

print(listedeki_en_buyuk_iki_sayi(sayilar))

## Map, Filter ve Lambda Uygulamalari

#### Soru 4: Asagidaki fonskiyonu 1 parametre alacak (liste tipinde) ve sadece str tipindeki degerleri filter ve lambda ifadelerini kullanarak filtreleyecek bicimde olusturun
sonuc= []
def str_filtrele(list):
    for x in list:
        if type(x) == str:
            sonuc.append(x)
        else:
            pass
    return sonuc

print(str_filtrele([1,2,3,5,'abc','a',True]))

def str_filtrele(liste):

    return [*filter(lambda x : x if type(x)== str else None,liste)]

print(str_filtrele([1,2,3,5,'abc','a',True]))


#### Soru 5: Asagidaki fonskiyonu 1 parametre alacak (sadece sayi iceren liste tipinde) ve map ve lambda ifadelerini kullanarak 6 sifir atacak bicimde olusturun
def paradan_alti_sifir_at(liste):
    sonuc=[]
    for x in liste:
        sonuc.append(int(x/1000000))

    return sonuc

print(paradan_alti_sifir_at([1000000, 90000000, 15000000]))

def paradan_alti_sifir_at(liste):
    return [*map(lambda x : int(x/1000000) ,liste)]

print(paradan_alti_sifir_at([1000000, 90000000, 15000000]))


## Kullanici Girdisi Uygulamasi

#### Soru 6: Asagidaki fonskiyonu input komutu ile kullanicidan saat ve dakika alacak bicimde olusuturun.
def zaman_verisi_al():

    saat = input("Saat giriniz:")
    if saat.isdigit():
        saat = int(saat)
        if((saat > 0 ) and (saat < 24)):
            dakika = input("Dakika giriniz:")
            if dakika.isdigit():
                dakika=int(dakika)
                if((dakika>0) and (dakika<60)):
                    return 'Giris Yapilan Zaman {}:{}'.format(saat,dakika)
                else:
                    print("Girilen dakika araligi yanlis")
            else:
                print("Girilen dakika yanlis veri tipinde")
        else:
            print("Girilen saat araliği yanlis")
    else:
        print("Girilen saat yanlis veri tipinde")

print(zaman_verisi_al())