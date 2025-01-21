'''
Check if a year input by the user is a century year.
A number can be a century year if it is 100% divisible by 100
and a year has to be in thousands i.e. 2000
Make sure user isn't able to enter something like 200 or 300 '''

year = int(input("Enter any year:\n"))

if year >= 1000:
    if year % 100 == 0:
        print(f"{year} is a century year.")
    else:
        print("No {year} isn't a century year.")
else:
    print("Enter a Valid Year")            