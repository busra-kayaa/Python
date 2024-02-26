# Döngüler ve sorgularla ilgili quiz

kullanici1 = {
    'ad': 'İrem',
    'soyad': 'Demir',
    'uzmanlik': ['Front-End']
}
kullanici2 = {
    'ad': 'Saziye',
    'soyad': 'Dağ',
    'uzmanlik': ['Tasarim']
}
kullanici3 = {
    'ad': 'Osman',
    'soyad': 'Can',
    'uzmanlik': ['Front-End']
}

# Soru 1: İrem Demir Kullanicisinin uzmanlik alanlarini döndür
print(kullanici1.get('uzmanlik'))
print(kullanici1['uzmanlik'])

kullanici_listesi = [kullanici1, kullanici2, kullanici3] 
# Soru 2: Front-end alanindaki uzmanlarin isimlerini döndür
print("\n")
for kullanici in kullanici_listesi:
    if 'Front-End' in kullanici.get('uzmanlik'):
        print(kullanici.get('ad'))

print("\n")
for kullanici in kullanici_listesi:
    if kullanici.get('uzmanlik')== ['Front-End']: # uzmanlığı sadece frontend olanları döndürür
        print(kullanici.get('ad'))

# Soru 3: Osman kullanicisi Yazilim ögrendi, bilgileri güncelle!
kullanici3['uzmanlik'].append('Yazilim')       
print(kullanici_listesi)

print("\n")
# Soru 4: 1den fazla uzmanlik alani olan kullanicilari döndür (Hint: length)
for kullanici in kullanici_listesi:
    if len(kullanici['uzmanlik']) >1:
        print(kullanici)

print("\n")
kullanici_yaslari_listesi = [22, 34, 32]
# Soru 5: zip kullanarak iki listeyi birlestir ve yasi 30'dan az olan kullanicilar kimler?
for kullanici,yas in zip (kullanici_listesi,kullanici_yaslari_listesi):
    if yas <30:
        print(kullanici)


# Soru 6: deger isimli degiskene atanan sayinin asal olup olmadigini söyle!
# Hint Asal sayi: kendinden ve 1'den baska böleni olmayan sayilar örnek 2,3,5,7
print("\n")
deger = 7
x = 2
while x < deger:
    if deger % x == 0:
        print('{} sayisi asal değil!'.format(deger))
        break
    else:
        x += 1
else:
    print('{} sayisi asaldir!'.format(deger))
