# 3 ve 2'yi toplamı için bu alanı kullanabilirsin:
print(3+2)

# 5 ve 4'ü çarpımı için bu alanı kullanabilirsin:
print(5*4)

# 5 ve 4'ün bölümünden kalan için bu alanı kullanabilirsin:
print(5%4)

# 2.3 ve 4.7'nin toplama işleminin neticesi hangi veri tipindedir?
print(type(2.3+4.7))

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
#  aradaki operatör >,< ise kullanılmaz.

# type(3) == type('3') sorgusunu cevap olarak ne döndürür?

print(type(3) == type('3')) 
