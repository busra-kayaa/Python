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
# Listenin 2. ve 4. elemanlarını içeren yeni bir liste oluştur (İpucu [::])
print(liste[2::])
# Listeyi metod kullanarak nasıl ters sıralarsınız?
liste.reverse()
# Listeyi [::] kullanarak nasıl ters sıralarsınız?

# Eğer yukarıdaki listeyi, set'e çevirecek olsak eleman sayısı farklı olur muydu? Neden?
# Evet olurdu çünkü 


ic_ice_liste = [1,2,3,[4,5]]
# 5 değerine nasıl ulaşırsınız?
