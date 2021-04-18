numbers = [1, 3, 7, 4, 3, 0, 6, 3, 7 ,8 ,4 ,4 ,4 ,6 ,7 ,6 ,5 ,4, 5, 4, ]
harf = ["a", "g", "h", "k", "l", "m", "f" , "d" , "s" ]
print(max(numbers))
print(max(harf))
print(numbers.count(3))

most_frequent = max(numbers, key = numbers.count) # Burada max() fonksiyonu keyi olarak count belirledik, ve listenin içinde en çok geçen elemanı verir
                                                  # count() fonksiyonu da bir list fonksiyonu olduğu için list ismi ile birlikte belirtilmelidir. len() fonksiyonunu key için kullanırken böyle birşey yok
repeat = numbers.count(most_frequent)

result = f"the most frequent number is {most_frequent} and it was {repeat} times repeated"
print(result)