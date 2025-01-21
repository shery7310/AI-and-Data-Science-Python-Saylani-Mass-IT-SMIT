# Write a function to check whether a string is a palindrome.

any_word = input("Enter Any String:\n").lower()

# lets say any_word = Ana
def is_palindrome(word:str):
    """
        Check if a given word is a palindrome.

        Args:
            word (str): The string to check.

        Returns:
            bool: True if the word is a palindrome, False otherwise.
        """
    flag = False # if any of the characters are not same flag remains False
    for char_num in range(1, len(word) + 1): # We want to compare strings using negative indexing, the negative indexing starts from 1
        # instead of 0 so we start it from 1 and end it 1 after the len(word) as the end in for loop is exclusive
        # These are the positive indexes for word if it was Ana. ['a', 'n', 'a'] indexes: [0, 1, 2] read from the left
        # These are the negative indexes for word Ana. [-3, -2, -1] start reading from the right
        # These are the numbers in char_num respectively: [1, 2, 3]
        # we are subtracting 1 from each char_num so character using positive indexing is checked against character at negative indexing
        # for example character at 1 - 1 for "Ana" will be a and character for -1 will also be a
        # 2 - 1 = 1 will be n and -2 will also be n
        if word[char_num - 1] == word[-char_num]:
            flag = True # if this is the case for each character the value is set to True again and again
    return flag

if is_palindrome(any_word):
    print(f"Yes, {any_word} is a Palindrome!")
else:
    print(f"No, {any_word} is not a Palindrome!")