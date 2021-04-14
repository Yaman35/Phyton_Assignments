"""Task : Find out if the given word is "comfortable words" in relation to the ten-finger keyboard use.

A comfortable word is a word which you can type always alternating the hand you type with (assuming you type using a Q-keyboard and use of the ten-fingers standard).
The word will always be a string consisting of only letters from a to z.
Write a program which returns True if it's a comfortable word or False otherwise.
Examples
Given  word	Desired Output (explanation)
tester	False (uses only left-hand fingers)*
polly	False (uses only right-hand fingers)*
clarusway	True (uses both hand fingers)*"""

left = set("qwertasdfghzxcvb")
right = set("üğpoıuyişlkjçömn")
word = set(input("Please enter a word: "))
result = bool(word.intersection(left)) and bool(word.intersection(right))
print(result)