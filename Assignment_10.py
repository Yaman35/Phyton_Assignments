
age = input("Are you a cigarette addict older than 75 years old: ")

if not age:
    print(input("Can't be blank, please answer:"))
elif age.lower() == "yes":
    age = True
elif age.lower() == "no":
    age = False
else:
    print("Please write your answer. As Yes or No")
            
    
chronicle = input("Do you have a severe chronic disease? Yes or No : ")
if not chronicle:
    print("Please, answer, can't be blanked")
elif chronicle.lower() == "yes":
    chronicle = True
elif chronicle.lower() == "no":
    chronicle = False
else:
    print("Please write your answer. As Yes or No ")

    
immune = input("Is your immune system too weak? Yes or No: ")
if not immune:
    print("Please, answer, can't be blanked")
elif immune.lower() == "yes":
    immune = True
elif immune.lower() == "no":
    immune = False
else:
    print("Please write your answer. As Yes or No")
    
    
if age or immune or chronicle:
    print("You are in risky group")
else:
    print("You are not in risky group")