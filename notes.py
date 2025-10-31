import random

#dosyayı okur
with open("motivation.txt", "r", encoding="utf-8") as dosya:     # with, bir context manager başlatıp iş bitince kaynakları otomatik temizler. "r" ile dosyayı okuma modunda açıyoruz.
    cumleler = dosya.readlines()                                 # .readlines() dasyayı okur ve her satırı sonundaki /n ile birlikte bir eleman olarak alır.

#rastgele seçim
secili = random.choice(cumleler)                                 # .choice() verilen koleksiyondan rastgele bir eleman döndürür

print(secili.strip())                                            # .strip() baş ve sondaki gereksiz karakterleri siler (örn. /n)

#.txt dosyasındaki satırların aralarına boşluk bırakırsan, 15 dk mal gibi niye boş sonuç dönüyor diye hata ararsın.

#_________________________________________


import random, string

uzunluk = int(input("şifre uzunluğu: "))
karakter = string.ascii_letters + string.digits + string.punctution
sifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))

print("oluşturulan şifre:", sifre)







