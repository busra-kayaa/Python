# Fonksiyonlar - Input - Try Except

#snake_case
def bes_bastir():
    print(5)

bes_bastir()

#docstring
def bes_bastir():
    """
    Fonksiyonu okuyan kişiye 
    yardim amacli yazilan ifadeler.
    Fonksiyonun ciktisini etkilemez.
    """
    print(5)

bes_bastir()

#return/ print
def bes_dondur():
    return 5

print(bes_dondur())

print("\n")
a=bes_bastir() #besbatirla 5 yazar ama print a none'dır.
print(a)

print("\n")
b=bes_dondur()
print(b)


def sayi_dondur(sayi):
    return sayi

print(sayi_dondur(596386))

print("\n")
def sayi_dondur(sayi=250): #default argüman 
    return sayi

print(sayi_dondur(89))
print(sayi_dondur()) #herhangi bir argüman vermeyince defaultu döndürür

print("\n")
def buyuk_sayi_dondur(a,b):
    if a>b:
        return a
    elif b>a:
        return b
    
print(buyuk_sayi_dondur(5,10))

print("\n")
def metin_yazdir(a,b):
    buyuk_sayi = buyuk_sayi_dondur(a,b)
    sablon_metin = "{} daha buyuk sayidir".format(buyuk_sayi)
    print(sablon_metin)

metin_yazdir(4,7)

print("\nBirden Fazla Sonuc Dondurme")
def isim_soyisim_ayirma(isim_soyisim):
    isim=isim_soyisim.split()[0]
    soyisim=isim_soyisim.split()[1]
    return isim,soyisim

print(isim_soyisim_ayirma("Büsra Kaya"))

a,b=isim_soyisim_ayirma("Büsra Kaya")
print(a)
print(b)

# *args argümanı
"-".join(["Büşra","Kaya"])

def isim_soyisim_birlestir(isim,soyisim):
    return " ".join([isim,soyisim])

print(isim_soyisim_birlestir("Bety","Badem"))
# print(isim_soyisim_birlestir("Hasan","Basri","Kaya")) #iki isimli olunca hata veriyor

def isim_soyisim_birlestir(*args): #args listeye referans veriyor
    return " ".join(args)

print(isim_soyisim_birlestir("Hasan","Basri","Kaya"))
print(isim_soyisim_birlestir("Omer","Faruk","Kaya"))
print("\n")

def isim_soyisim_birlestir(*args):
    for item in args:
        print(item)
    return " ".join(args)

isim_soyisim_birlestir("Omer","Faruk","Kaya")
print("\n")

def gobek_adi_yazdir(**kwargs): #keyword argümanda dictionary olarak tutulur
    if 'gobekadi' in kwargs:
        print(kwargs['gobekadi'])
    else:
        print("Gobekadi yok")

gobek_adi_yazdir(adi="Büşra", gobekadi="Kübra", soyadi="Kaya")
gobek_adi_yazdir(adi="Betül",soyadi="Badem")

#### Map -> listenin her elemanına aynı fonksiyonu uygulamayı sağlıyor
def karesini_al(x):
    return x**2 # karesini alma işlemi
print(karesini_al(5))

print("\n")
sayilar = list(range(1,6)) # [*range(1,6)]
print(sayilar)
for index in range(len(sayilar)):
    sayilar[index] = karesini_al(sayilar[index])
print(sayilar)

print("\n")
sayilar =[*range(1,6)]
print([*map(karesini_al,sayilar)])

#### Filter -> filtrelemeye yarıyor
print("\n")
def cift_sayilari_filtrele(x):
    if x%2==0:
        return x
    else:
        return None

print(cift_sayilari_filtrele(4))
print(cift_sayilari_filtrele(3))

print("\n")
def cift_sayilari_filtrele(x):
    return x if x%2==0 else None

print(cift_sayilari_filtrele(5))
print(cift_sayilari_filtrele(6))

sayilar =[*range(1,6)]
print([*filter(cift_sayilari_filtrele,sayilar)])
print("\n")

#### Lambda -> fonksiyon oluşturmadan işlevselliği oluşturmayı sağlıyor
sayilar =[*range(1,6)]
print(list(map(lambda sayi: sayi**2,sayilar)))

sayilar =[*range(1,6)]
print(list(filter(lambda x: x if x%2==0 else None,sayilar)))
print([*filter(lambda x: x if x%2==0 else None,sayilar)])
print("\n")

# Kullanici girdisi almak
girdi=input("Bir sayi giriniz:")
print(type(girdi)) # str

girdi=input("Bir sayi giriniz:")
print(type(int(girdi))) #int

def uygulama():
    girdi=input("Bir sayi giriniz:")
    islem=input("Verinin tek mi cift mi oldugunu sorgula:")

    if islem=='cift':
        if int(girdi)%2==0:
            return 'Evet {} sayisi bir cift sayidir'.format(girdi)
        else:
            return 'Hayir {} bir cift sayi degildir'.format(girdi)
        
    elif islem=='tek':
        if int(girdi)%2==1:
            return 'Evet {} bir tek sayidir'.format(girdi)
        else:
            return 'Hayir {} bir tek sayi degildir'.format(girdi)

sonuc = uygulama()
print(sonuc)

# Kullanici girdisini onaylamak
def sayi_girdisi_kontrol():
    girdi=input("Bir sayi giriniz:")

    if girdi.isdigit():
        print("Tebrikler! Sayi tipi deger girdiniz")
    else:
        print("Uzgunum! Bu bir sayi tipi degisken değildir")

sayi_girdisi_kontrol()

def sayi_girdisi_kontrol_dongu():
    girdi=input("Bir sayi giriniz:")

    while not girdi.isdigit():
        print("Uzgunum! Bu bir sayi tipi degisken değildir")
        girdi=input("Bir sayi giriniz:")
    else:
        print("Tebrikler! Sayi tipi deger girdiniz")

sayi_girdisi_kontrol_dongu()
print("\n")
def eposta_kontrol():
    #busrakaya@hotmail.com , f22@ktun.edu.tr
    girdi= input("Gecerli e posta adresi giriniz:")

    while not( ('.'in girdi) and ('@'in girdi)):
        print("Üzgünüm! Bu gecerli bir eposta adresi değil...")
        girdi= input("Gecerli e posta adresi giriniz:")
    else:
        print("Tebrikler! eposta adresinizle basariyla giriş yaptiniz")

eposta_kontrol()

# Try Except Finally
print(round(1.6)) # Ondalıklı sayıyı en yakin tam sayiya yuvarlar

def tam_sayiya_cevir():
    girdi=input("bir ondalik sayi giriniz:")

    print("Yuvarlama işleminin sonucu: {}".format(round(float(girdi))))

tam_sayiya_cevir()
# a value error verir

def tam_sayiya_cevir():
    girdi=input("bir ondalik sayi giriniz:")

    try:
        girdi = float(girdi)
        print("Yuvarlama işleminin sonucu: {}".format(round(girdi)))
    except:
        print("{} girdisi ondalik tipe cevrilemedi".format(girdi))

tam_sayiya_cevir()

def tam_sayiya_cevir():
    girdi=input("bir ondalik sayi giriniz:")

    try:
        girdi = float(girdi)
        print("Yuvarlama işleminin sonucu: {}".format(round(girdi)))
    except:
        print("{} girdisi ondalik tipe cevrilemedi".format(girdi))

tam_sayiya_cevir()

def tam_sayiya_cevir():
    girdi=input("bir ondalik sayi giriniz:")

    try:
        girdi = float(girdi)
    except:
        print("{} girdisi ondalik tipe cevrilemedi".format(girdi))
    else:
        print("Yuvarlama işleminin sonucu: {}".format(round(girdi)))

tam_sayiya_cevir()

print("\n")
def tam_sayiya_cevir():
    girdi=input("bir ondalik sayi giriniz:")
    status=''
    try:
        girdi = float(girdi)
        print("Yuvarlama işleminin sonucu: {}".format(round(girdi)))
        status='basarili'
    except:
        print("{} girdisi ondalik tipe cevrilemedi".format(girdi))
        status='basarisiz'
    finally:
        print("Tam sayiya cevirme işlemi {} olarak tamamlandi!".format(status))
        
tam_sayiya_cevir()

def tam_sayiya_cevir_dongu(): 
    while True:
        girdi=input("bir ondalik sayi giriniz:")
        try:
            girdi = float(girdi)
            print("Yuvarlama işleminin sonucu: {}".format(round(girdi)))
            break
        except:
            print("{} girdisi ondalik tipe cevrilemedi".format(girdi))
            pass

tam_sayiya_cevir()

# type error
# print(5 +'a') # int +str
try:
    5 +'a'
except TypeError:
    print('Girilen verilerle islem yapilamaz')

try:
    5 +'a'
except IndexError:
    print('Girilen verilerle islem yapilamaz')
except:
    print("Kod duzgun calismiyor")

# index error
liste=[]
# print(liste[4]) #list index out of range

liste=[]
try:
    print(liste[-1])
except IndexError:
    print("Indexlemeye calistiginiz eleman listenin disinda")
except:
    print("Kod duzgun calismiyor")

#key error
vatandas = {
    'Ad': 'Oguz',
    'Tc_No':121212  
}
#print(vatandas['Pass_No'])

vatandas = {
    'Ad': 'Oguz',
    'Tc_No':121212  
}
try:
    print(vatandas['Pass_No'])
except IndexError:
    print("Indexlemeye calistiginiz eleman listenin disinda"),
except KeyError:
    print("Aranan dictionaryde verilen anahtar degeri mevcut değil")
except:
    print("Kod duzgun calismiyor")



