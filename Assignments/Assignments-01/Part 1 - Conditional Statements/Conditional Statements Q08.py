# Create a program that checks if a given string is a palindrome.

palindrome = input("Enter any palindrome:\n").lower()

reverse = palindrome[::-1]
if palindrome == reverse:
    print("Yay Man This is a palindrome")
else:
    print("This isn't a palindrome")   


'''

Some words we can check against:
Level, Radar, Civic, Noon, Racecar, Refer, Madam, Rotator, Deified, Kayak
'''    