# Write a program that continues to ask for a number until
# the correct number is guessed.

nums = '173942006000'
print("Guess a number, a single digit or multi-digit one:")
guess = input()

condition = True
while condition == True:
    if guess not in nums:
        print("You guessed it wrong, guess again")
        guess = input()
    elif guess in nums:
        print("You guessed it—great!")
        condition = False        