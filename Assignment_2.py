"""Write a short Python program that asks the user to enter Celsius temperature (it can be a decimal number), 
converts the entered temperature into Fahrenheit degree and prints the result."""

cels = float(input("Please enter the Celcius Temperature: "))
fahr = cels * 1.8 + 32
print(str(cels) + " Celcius equals to " + str(fahr) + " Fahreneit!")



"""Write a short Python program that asks the user to enter a distance (it can be a decimal number) in kilometers, 
converts the entered distance into miles and prints the result."""

km = float(input("Please enter the kilometer to be converted to mile: "))
mile = km * 0.62137

print(str(km) + " kilometers equals to "+ str(mile) + " miles") 
