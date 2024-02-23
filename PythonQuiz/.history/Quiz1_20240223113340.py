# 3 ve 2'yi toplamı için bu alanı kullanabilirsin:
print(3+2)

# 5 ve 4'ü çarpımı için bu alanı kullanabilirsin:
print(5*4)

# 5 ve 4'ün bölümünden kalan için bu alanı kullanabilirsin:
print(5%4)

# 2.3 ve 4.7'nin toplama işleminin neticesi hangi veri tipindedir?
print(type(2.3+4.7)) #float

strvar = 'Yakin Kampüs'
# "ü" harfini index komutu kullanmadan döndür.
print(strvar[10])

# "ü" harfinin konumunu, index komutu kullanarak döndür
print(strvar.index('ü'))

# strvar.upper().lower() ifadesinin cevabi nedir?
print(strvar.upper().lower()) #hepsi küçük harfle yazılır

# split() komutunu boşluk(space) dışında başka bir parametre ile kullan.
print(strvar.split('a'))

a = True
b = False
c = 'True'

# a == b sorgusu cevap olarak ne döndürür?
print(a==b) # true==false , false döndürür.

# a == c sorgusu cevap olarak ne döndürür?
print(a==c) #c string  a boolean eşit olmayacağından false döndürür.

# a!=b sorgusu cevap olarak ne döndürür?
print(a!=b) 

# ! ve not hangi senaryoda birbirinin yerine kullanilamaz? 
#  aradaki operatör >,< ise ! kullanılmaz ama not ifadesi kullanilabilir.

# type(3) == type('3') sorgusunu cevap olarak ne döndürür?
print(type(3) == type('3')) #integer == string false olur

liste = [1, 'a', 2, 3, True, 4, 5, 'True', '1']
# Listenin son elemanını nasıl bulabiliriz?
print(liste[-1])

# Listenin 2. ve 4. elemanlarını içeren yeni bir liste oluştur.
print(liste[2:6:3])

# Listeyi metod kullanarak nasıl ters sıralarsınız?
liste.reverse()
print(liste)

# Listeyi [::] kullanarak nasıl ters sıralarsınız?
liste = [1, 'a', 2, 3, True, 4, 5, 'True', '1']
print(liste[::-1])

# Eğer yukarıdaki listeyi, set'e çevirecek olsak eleman sayısı farklı olur muydu? Neden?
# Olmazdi cunku her eleman 1 defa tekrar ediyor, ama True'yu teke indirgiyor!
print(len(liste)==len(set(liste)))

ic_ice_liste = [1,2,3,[4,5]]
# 5 değerine nasıl ulaşırsınız?
print(ic_ice_liste[3][1])
print(ic_ice_liste[-1][1])

#  ic_ice_liste değişkeninin son konumunda bulunan elemanını listeden atın ve bu kısmı bir degişkene atayın
atilan=ic_ice_liste.pop()
print(atilan)

#  pop komutunu kullanmayarak listeyi nasil [1,2,[4,5]] sekline cevirebilirsiniz?
ic_ice_liste = [1,2,3,[4,5]]
yeni = ic_ice_liste[:2] + [ic_ice_liste[-1]]
print(yeni)

# Dictionary veri tipinin listeden farkı nedir?
# Dictionaryde sıranın bir önemi yoktur. Çok boyutludur.

# Dictionary oluştururken kullanılan anahtar ve değer çiftinin Python'daki karşılıkları nelerdir?
# key -> value

my_dict = {'isim': 'Mesut', 'yas':32, 'lokasyon': {'yasadigi':'Berlin', 'dogdugu': 'Istanbul'}}
# 32 değerine nasıl ulaşırsınız?
print(my_dict['yas'])
print(my_dict.get('yas'))

# isim anahtarına karşılık gelen değeri, kendi isminizle değiştirin:
my_dict['isim'] = 'Büşra'
print(my_dict)

# my_dict değişkenindeki 'Istanbul' değerine nasıl ulaşabiliriz?
print(my_dict['lokasyon']['dogdugu'])
print(my_dict.get('lokasyon').get('dogdugu'))

# my_dict değişkenindeki bütün anahtar değerlerine nasıl ulaşırız?
print(my_dict.keys())

# Tuple ile liste arasındaki farklar nelerdir?
# Tuple immutabledir yani degisimez.

# print komutu ile ve print komutsuz yazdırmanın farkı nedir? Her durumda birbiri yerine kullanılabilir mi?
# print ile istenilen kadar satır yazılabilir ama print kullanılmayinca sadece son satir yazilir.

# String ifadelerinin içerisinde \t ile \n kullanmanın farkı nedir?
#\t bir tab bosluk koyar, \n yeni satıra geçer.

# değişken isimlendirmelerinde dikkat edilmesi gereken hususlar nelerdir?
# değişken aralarına bosluk konulamaz, degisken ismi sayi ile baslayamaz.

# [] {} ve () işaretlerini veri tipleri ile eşleştirin:
# '' -> String 
# [] -> 
# {} -> 
# () ->