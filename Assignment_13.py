# Çözüm - 1

default = 1  # Listeye 1 elemanını default olarak eklemek için
fibonacci_list = [default]
while fibonacci_list[-1] < 55: # Fibonacci listemizin son elemanı 55 den küçük olduğu sürece işleme devam eder
    fibonacci_list.append(sum(fibonacci_list[-2:])) # Listenin son iki elemanının toplamını her daim listeye eklemek için
print(fibonacci_list)

# Çözüm -2 

number=1
a=0
liste = [number]
for i in range(number,56):
    if i == number:
        liste.append(number)
        a += 1
        number += liste[a-1]
print(liste)