# Write a program to determine if a given character is a vowel or consonant.
# A consonant is a speech sound that is not a vowel.

char = input("Enter any character:\n")

if char == 'a' or 'e' or 'i' or 'o' or 'u':
    print(f"{char} is a vowel.")
else:
    print(f"{char} is a consonant.")

# We could also check this like this:

# vowels = 'aeiou'
# if char in vowels:
#     print(f"{char} is a vowel.")