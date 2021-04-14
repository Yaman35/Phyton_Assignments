"""Task : Find out if the given word is "comfortable words" in relation to the ten-finger keyboard use.

A comfortable word is a word which you can type always alternating the hand you type with (assuming you type using a Q-keyboard and use of the ten-fingers standard).
The word will always be a string consisting of only letters from a to z.
Write a program which returns True if it's a comfortable word or False otherwise.
Examples
Given  word	Desired Output (explanation)
tester	False (uses only left-hand fingers)*
polly	False (uses only right-hand fingers)*
clarusway	True (uses both hand fingers)*"""      

left = set("qwertasdfghzxcvb") # Sol el harflerini bir küme yaptık 
right = set("üğpoıuyişlkjçömn") # Sağ el harflerini bir küme yaptık
word = set(input("Please enter a word: ")) #Kullanıcıdan bir kelime aldık ve kümeye attık
result = bool(word.intersection(left)) and bool(word.intersection(right)) # Kullanıcının girdiği kelime kümesi ile sol-sağ el kümelerinin bir kesişimi olup olmadığına baktık
print(result)                                                             # Varsa zaten boolean olarak True yoksa False döner 
print(word.intersection(left)) 
print(word.intersection(right))                                                          


# Bir başka çözüm (specific kelimeler için)
# left_hand = {"q", "a", "z", "w", "s", "x", "e", "d", "c", "r", "f", "v", "t", "g", "b"}
# right_hand = {"y", "h", "n", "u", "j", "m", "ı", "k", "ö", "o", "l", "ç", "p", "ş", "ğ", "ü", "i"}

# tester = set("tester")
# polly = set("polly")
# clarus = set("clarus")

# print("tester is comfortable word :",  tester.issubset(left_hand) and tester.issubset(right_hand))
# print("polly is comfortable word :",  polly.issubset(left_hand) and polly.issubset(right_hand))
# print("clarus is comfortable word :", not clarus.issubset(left_hand) and not clarus.issubset(right_hand))