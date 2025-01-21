# Create a function to generate a random password of given length,
# containing uppercase, lowercase, numbers, and special characters.
import random

letters = {
    1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e',
    6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
    11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o',
    16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
    21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
}

special_characters = (
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '=', '+', '[', ']', '{', '}', '|', '\\', ';',
    ':', '"', '\'', '<', '>', ',', '.', '?', '/',
    '~', '`', '_', ':', '$', '(', ')', '[', ']',
    '^', '&', '%', '*', '+', '-', '=', '|', '\\',
    '!', '@', '#', '$', '<', '>', '{', '}', ':',
    '"', '\'', '/', '?', ';', ',', '.', '¬', '©',
    '®', '™', '°', '¶', '÷', '×', '≈', '≠', '∑', '∏',
    '√', '∞', '∫', 'Δ', 'π', 'µ', 'λ', 'χ', 'α', 'β'
)


def convert_upper(letter):
    return letter.upper()

def convert_lower(letter):
    return letter.lower()

def generate_alphabets():
    capital_or_small = (convert_upper, convert_lower)
    number_of_steps = random.randint(1, 27) # A-Z are 26 characters
    letter_size = random.randrange(0,2)
    num = random.randrange(1, len(letters) + 1, number_of_steps) # generates unique number from 1 to 26
                                                                  # I made this to generate an alphabet
    alphabet_random = capital_or_small[letter_size](letters[num]) # will either return a capital or small alphabet for the current random number
    return alphabet_random # example returns S

def generate_numbers():
    num = random.randint(10, 10_0000)
    return str(num) # example returns 999

def generate_special_characters():
    num = random.randint(0, len(special_characters) - 1)
    return special_characters[num] # example returns &

def generate_pass():

    print("What's the length of password that you want?")
    pass_len = int(input())
    passwd = ""
    while len(passwd) < pass_len:

        passwd += generate_special_characters() # returns 1 character
        passwd += generate_alphabets() # returns 1 character
        passwd += generate_numbers() # can return any unknown number of characters between 10 and 10_0000
        passwd += generate_special_characters()
        passwd += generate_alphabets()
        passwd += generate_alphabets()
        passwd += generate_numbers()
        passwd += generate_special_characters()

    if len(passwd) > pass_len:
        passwd = passwd[0:pass_len] # since generate_numbers can generate any number of numbers we need to
                                    # make sure that password length remains what the user asked for
    return passwd

def ask_user():
    while True:
        password = generate_pass()
        print(f"Here is your Password: {password}")
        print("Would You Like another password? enter y for yes and q to quit")
        user_choice = input().lower()

        if user_choice == 'q':
            break
        else:
            password = generate_pass()
            print(f"Here is your Password: {password}")
            print("Would You Like another password? enter y for yes and q to quit")

ask_user()