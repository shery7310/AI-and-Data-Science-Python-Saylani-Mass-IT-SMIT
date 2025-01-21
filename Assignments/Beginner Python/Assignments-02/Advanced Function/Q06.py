# Create a function that takes a string and counts the frequency of each character.
# we are using python's builtin function list.count to count instances of a character in list

word = input("Enter a string:\n").lower()
char_counts = {}
def count_characters(word):
    for char in word:
        char_counts[char] = word.count(char)
    return char_counts

character_instances = count_characters(word)
for character, frequency in character_instances.items():
    print(f"{character} appeared {frequency} time(s) in String")