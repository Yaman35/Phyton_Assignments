number = input("Please enter a number : ")
sum = 0

while not number.isnumeric():
    number = input("It is an invalid entry. Don't use non-numeric, float, or negative values! : ")

for i in number:
    sum += int(i)**len(number)

if sum == int(number):
    print("It is an Armstrong Number!")
else:
    print("It is NOT an Armstrong Number!")

