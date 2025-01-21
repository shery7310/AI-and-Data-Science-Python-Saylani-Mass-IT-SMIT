"""
Take a user’s age as input and display whether they are a minor,
adult, or senior citizen

https://courtingthelaw.com/2017/12/27/commentary/legal-rights-of-children-under-laws-of-pakistan/
According to this source age of minor according to law in Pakistan is less than equal to 18
but anyone having a guardian his age should be less than equal to 21

"""

age = int(input("Enter Your Age:\n"))
guardian = input("Do you have a guardians other than Parents? (y, n)\n").lower()

if guardian == 'y':
      guardian == True


if guardian:
    if age <= 21:
        print("You are a minor according to some laws")
    elif age > 21 and age < 60:
        print("You are an adult")
    else:
        print("Respected Sir you are a Senior Citizen")
else:
    if age <=18:
        print("You are a minor according to some laws")
    elif age >18 and age < 60:
        print("You are an adult")
    else:
        print("Respected Sir you are a Senior Citizen")    



