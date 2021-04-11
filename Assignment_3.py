"""Problem :

Task : Estimating the risk of death from coronavirus.

Consider the following questions in terms of True/False regarding anyone else.

Are you a cigarette addict older than 75 years old? Variable → age

Do you have a severe chronic disease? Variable → chronic

Is your immune system too weak? Variable → immune

Set a logical algorithm using boolean logic operators (and/or) and the given variables 
in order to give us True (there is a risk of death) or False (there is not a risk of death) as a result."""

# Çözüm 1:

print("Please if it is true enter yes but if it is not leave it blank and press enter!")
age = input("Are you a cigarette addict older than 75 years old?: ")
chronic = input("Do you have a severe chronic disease?: ")
immune = input("Is your immune system too weak?: ")

result = bool(age) or bool(chronic) or bool(immune)
if result:                           # Bu kullanım eğer sonuç True ise anlamına gelir
  print("There is a risk of death")
else:                                # Burası da değilse
  print("There is NOT a risk of death")


# Çözüm 2:

  print("Please if it is true enter yes but if it is not leave it blank and press enter!")
age = bool(input("Are you a cigarette addict older than 75 years old?"))
chronic = bool(input("Do you have a severe chronic disease?"))
immune = bool(input("Is your immune system too weak?"))

result = age or chronic or immune
if result:                           # Bu kullanım eğer sonuç True ise anlamına gelir
  print("There is a risk of death")
else:                                # Burası da değilse 
  print("There is not a risk of death") 
