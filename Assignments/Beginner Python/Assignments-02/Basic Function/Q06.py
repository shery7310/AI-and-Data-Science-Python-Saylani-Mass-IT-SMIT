""" Write a function to count the vowels in a given string.
these are vowels: a, e, i, o, u """

vowels_in_each_word = {}
sentence = input("Enter A Sentence:\n").split(" ") # this splitting a sentence string if a space occurs, each word is then stored into a list
                                                   # so sentence is essentially a list now
def is_vowel(user_input_sentence):

    vowels = ('a', 'e', 'i', 'o', 'u')
    for word_num in range(len(user_input_sentence)): # this is give us each word in the list sentence (a list is being passed)
        vowel_ch = ""                                # this is an empty string each time after the nested for loop runs it again becomes empty
        for ch in user_input_sentence[word_num]:     # this is a nested for loop extracting each character of each word inside the list
            if ch in vowels:                         # if character is in the list vowels then the if statement is hit
                vowel_ch += ch                       # every time while the characters from a single word are traversed the character
                                                     # that is in the vowels list is appended to vowel_ch list
                                                     # If a word like Banana comes the vowel_ch string will store the first a, then the second
                                                     # a and then the third a i.e. vowel_ch will look like aaa
                vowels_in_each_word[word_num] = vowel_ch # The variable 'aaa' will be stored in a global dictionary
                                                         # The key represents the position of the word in the current sentence, starting at 0
                                                         # For example, the dictionary would have an entry like {0: 'aaa'}


    show_vowels(sentence)  # here we are calling another function, after first function's work is done the second one is being called
                           # we are also passing the exact sentence that is_vowel has
                           # if we call show_vowels inside any for loop it will call be called after each vowel is appended to the dictionary
                           # this isn't required but we can see that here a function can be used exactly like a variable
                           # let's say we call show_vowels() inside the if in nested loop a user enters the word like Procrastinate
                           # Then something like this will happen:
                           # The word "Procrastinate" has 1 vowel(s) which is/are: o
                           # The word "Procrastinate" has 2 vowel(s) which is/are: oa
                           # The word "Procrastinate" has 3 vowel(s) which is/are: oai
                           # The word "Procrastinate" has 4 vowel(s) which is/are: oaia
                           # The word "Procrastinate" has 5 vowel(s) which is/are: oaiae
def show_vowels(user_input_sentence):

    for word_num in range(len(user_input_sentence)):
        # Here we are running a for loop again on the passed sentence and each number of sentence is being stored in word_num
        if word_num in vowels_in_each_word: # Since Each Word is only appended with a word_num i.e 1, 2 or 3 if it has vowels
                                            # Therefore if a word_num i.e. 0 or 1 etc in inside the dict vowel_in_each_word
                                            # only then this if statement will be triggered
                                            # user_input_sentence[word_num] fetches the current word
                                            # len(vowels_in_each_word[word_num]) fetches number of vowels in vowel_ch for each word
                                            # vowels_in_each_word[word_num] fetches vowels for each word
            print(f'The word "{user_input_sentence[word_num]}" has {len(vowels_in_each_word[word_num])} vowel(s) which is/are: {vowels_in_each_word[word_num]}')
        else:
            print(f'The word "{user_input_sentence[word_num]}" has no vowels') # hitting else means that the current word has no vowels

is_vowel(sentence) #is_vowel is being called

