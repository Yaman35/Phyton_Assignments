number = int(input("Please enter a number : "))

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is NOT a prime number! Because it is {i} times {int(number / i)}")
            break
    else:
        print(f"{number} is a prime number!")       
else:
    print(f"{number} is NOT a prime number!")