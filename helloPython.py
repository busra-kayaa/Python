print("Selam")
print("Merhaba \nYeni Satir")
print("Benim Adim\tBüşra")

print("Benim adim {}".format('Büşra'))
print("Benim adim {}, yasim {}".format('Büşra',20))

print("Benim adim {0}, yasim {1}".format ('Büşra',20))
print("Benim adim {1}, yasim {0}".format ('Büşra',20))

print("Benim adim {ad}, yasim {yas}".format(ad='Büşra', yas=20))
print("Benim adim {ad}, yasim {yas}".format(yas=20, ad='Büşra')) 

sayi=10
print(sayi)

sayi=11
print(sayi)

sayi=sayi+1
print(sayi)

sayi_ilk = 10
print(sayi_ilk)

tip=type(3)
print(tip)

tip=type(1.5)
print(tip)

print(3.1*2.0)
print(3.0*5)

strvar = "python"
print(strvar)

print(strvar[-3])

print(strvar[2:])

print(strvar[:3]) # en bastan başlar.

print(strvar[2:5]) # ilki dahil ikinci değildir.

print(strvar[::2]) # iki iki atlar.

print(strvar[1:5:3]) # 1 den 5'e kadar 3 atlayarak 3.yü yazar.

print(len(strvar)) # uzunluk

print(strvar + " ogren!")
strvar = strvar + " ogren!"

print(strvar*3)

print(strvar.upper())
print(strvar.lower())

print(strvar.split())
print(strvar.split("o"))
print(strvar.split(sep="o", maxsplit=1))

a = True
b = False

print(a)
print(type(a))
print(b)

c = 'True'
print(c)
print(type(c))

yas1=20
yas2=18

print(yas1>18)
print(yas2>18)

print(yas2==18)
print(yas1==18)

print(yas2 != 18)
print(yas1 != 18)

print(not yas2 > 18)

liste = ['a','b','c','d','e','a']
print(liste)

# liste = liste + 'f' # çalışmaz
liste = liste + ['f']
print(liste)

print(liste[0])
print(liste[3:5])

liste.append('g')
print(liste)

liste.pop() # 'g'
print(liste)

liste.pop(5)
print(liste)

sayilar = [123,12321,312,45435,35,345,1,1]
sayilar.sort() # listeden rakam atmaz sıralama yapar sadece
print(sayilar)

sayilar.reverse()
print(sayilar)

print(set(sayilar))

liste = ['a','b','c','d','e','a']
print(liste)

tup = ('a','b','c','d','e','a')
print(tup)

liste[0] = 12312
print(liste)

# tup[0] = 12312 #değiştirilemez.
print(tup) # değişemedi

print(tup[0])
print(tup[0:3])

print(tup.count('a'))
print(tup.count('b'))
print(tup.count(True))

print(tup.index('b'))
print(tup.index('a'))
# print(tup.index(True)) # value error verir True not in Tuple

dict1 = {'isim':'Busra', 'yas':20,'lokasyon': 'Berlin'}
print(dict1)

dict2 =  {
    'isim':'Busra',
    'yas':20 ,
    'lokasyon': 'Konya'
}
print(dict2)

dict3 ={
    'isim':'Busra',
    'yas':20 ,
    'lokasyon': { 
        'dogduguSehir': 'Ankara',
        'yasadigiSehir': 'Konya'
        }
}
print(dict3)

print(dict2['yas'])
print(dict3['lokasyon'])
print(dict3['lokasyon']['yasadigiSehir'])

print(dict2.get('yas'))
print(dict3.get('lokasyon'))

print(dict3.keys())
print(dict3.values())
print(dict2.items())

