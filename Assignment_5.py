"""Artık yıl hesaplama

Öncelikle algoritmamızın temal mantığını işleyecek kodları yazalım. algoritmamızın çözmesi gereken problem:

1- 4 ile bölünen yıllar artık yıldır.
2- 400 ile bölünen yıllar artık yıldır.
3- 100 tam katı olan yıllar artık yıl değildir 
Sonuç: 4 veya 400 ile tam bölünüp 100'ün katı olmayan yıllar artık yıldır.'
 
istenilen: Kullanıcıdan 4 defa 4 haneli tarih bilgisi girmesi isteniyor.
girilen yılların artık yıl olup olmadığı sorgulanıp ekran yazdırılacak.
ilk önce kullanıcıdan veri alıp bunu işleyen ve temel kodları yazalım. Sonra
gerekli istenilen yan düzenlemeleri yapalım."""

# Çözüm 1:

year = int(input("Gireceğiniz yıl artık yıl mı değil mi?: "))

result = (year % 4 == 0) and (year % 400 == 0) or (year % 100 != 0) # 4 ve 400 e kesin bölünmeli 100 e bölünmese de olur mantığıyla
print(result)


# Çözüm 2:

year = int(input("Lütfen 4 haneli olacak şekilde yıl giriniz: "))

if year % 4 == 0 and year % 100 == 0:
    if year % 400 == 0:
        print(f"{year} artık yıldır.")
    else:
        print(f"{year} artık yıl değildir. ")
elif year % 4 == 0:
    print(f"{year} artık yıldır")
else:
    print(f"{year} artık yıl değildir. ")