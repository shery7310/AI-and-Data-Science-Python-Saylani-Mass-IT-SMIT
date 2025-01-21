# Write a Python program to split a dictionary into two based on whether the
# values are odd or even.
import random
alphabets = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

def make_random_num(): # This randomly creates a number from 1000 to 10000
    num = random.randrange(1000, 10_001)
    return num

evens = {}
for alphabet in alphabets: #This loop will run 26 times
    num = make_random_num() # Each time a random number will be stored in num
    if num % 2 == 0: # If that number is even it will be added to the dictionary evens
        evens.update({alphabet: num})

odds = {}
for alphabet in alphabets:
    num = make_random_num()
    if num % 2 != 0: # If that number is odd it will be added to the dictionary odds
        odds.update({alphabet: num})

# We could haved solve these using dictionary comprehensions and filter