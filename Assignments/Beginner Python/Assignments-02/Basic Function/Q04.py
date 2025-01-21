# Write a function that takes a string and returns it reversed.

word = input("Enter any string:\n")

reversed_word = "" # global variable
def reverse_word(string):
    global reversed_word # this helps change value of variable outside the scope of this function
    for i in range(1, len(string) + 1):
    # here the loops is traversing in reverse fashion
    # for example the user enter the string word, the last element
    # of the string has index of -1, then comes -2, then -3 and the first one from negative indexing is -4
    # so we are using negative indexing to reverse the string
    # and concatenating the empty string called reversed_word
        reversed_word += word[-i]

    return reversed_word

print(f"The word reversed is {reverse_word(word)}")