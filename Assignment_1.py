"""If you had deposited a coin on the cryptocurrency exchange that brought 7% fixed profit daily for a week, 
how much would your $ 1000 reach at the end of the 7th day?"""

a1 = 1000
a2 = (a1 / 100)*7
a = a1 + a2

b1 = a
b2 = (b1 / 100)*7
b = b1 + b2

c1 = b
c2 = (c1 / 100)*7
c = c1 + c2

d1 = c
d2 = (d1 / 100)*7
d = d1 + d2

e1 = d
e2 = (e1 / 100)*7
e = e1 + e2

f1 = e
f2 = (f1 / 100)*7
f = f1 + f2

h1 = f
h2 = (h1 / 100)*7
h = h1 + h2

print('My 1000$ after 1 week becomes: ' + str(h) + '$')



# for döngüsü ile çözümü

toplam = 1000

for i in range(7): # Bu işlemi 7 kez yap demektir
  toplam += (toplam*7) / 100

print(toplam)


# Tek satır çözümü

print(1000 * 1.07 ** 7)