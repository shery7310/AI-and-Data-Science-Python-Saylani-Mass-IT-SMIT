# Check if a string input is uppercase, lowercase, or a mix.

string = input("Enter a string:\n")
if string.islower() == True:
    print(f"'{string}' is in lowercase.")
elif string.isupper() == True:
    print(f"'{string}' is in uppercase.")
else:
    print(f"'{string}' is a mixed string.")  

'''
isupper() and islower() are built-in python string functions that return True or False.
If all alphabets in the string are uppercase the isupper() will return True.
If all alphabets in the string are lowercase the islower() will return True.
If neither of these conditions are met this means that the string is a mixed one.
'''    