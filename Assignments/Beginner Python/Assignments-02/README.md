### Basic Function Questions

1. Write a function to calculate the area of a circle given its radius.
2. Create a function that takes two numbers and returns their sum.
3. Write a function to find the factorial of a number using recursion.
4. Write a function that takes a string and returns it reversed.
5. Create a function to check if a given number is prime.
6. Write a function to count the vowels in a given string.

### Intermediate Function Questions

1. Create a function that takes a list of numbers and returns the largest number.
2. Write a function to find the nth Fibonacci number using recursion.
3. Write a function to check whether a string is a palindrome.
4. Create a function that takes a list of integers and returns the sum of all even numbers.
5. Write a function to calculate the GCD (Greatest Common Divisor) of two numbers.
6. Create a function that accepts a dictionary and returns the key with the highest value.

### Advanced Function Questions

1. Write a function that calculates the power of a number without using the ** operator.
2. Create a function that converts a given temperature from Celsius to Fahrenheit and vice versa.
3. Write a function to flatten a nested list.
4. Create a function to check if two strings are anagrams.
5. Write a function that takes a list and removes all duplicate elements.
6. Create a function that takes a string and counts the frequency of each character.

### Real-world Scenarios

1. Write a function that takes a list of employee salaries and calculates the average salary.
2. Create a function to generate a random password of given length, containing uppercase, lowercase, numbers, and special characters.

## Some Questions That I found Interesting 
### Finding Maximum Value in a list


![](https://i.imgur.com/7aIQIST.png)

This can be found at: https://excalidraw.com/#json=m4bWt2DSERIDiD8_xPjR4,qADyfXhbbcj1v6m9IQ-aHw

Although this isn't the most efficient solution the program keeps on running until the largest value in a list reaches the **end** of the list. And the end we are returning that last element of the list as you can see in the image that 30 starts from index 0 and reaches index -1 (negative indexing). In Iteration 1 the loop starts comparing the first two numbers 30 and 21, if the first number is greater than the second number than they will be replaced else nothing will happen. So 30 comes in place of 21 and 21 comes in place of 30 and this keeps happening in each iteration the sliding window keeps on changing i.e. 

![](https://i.imgur.com/Ij222NJ.png)

The green combination of first and second variable is like a sliding window and we are comparing each element in each iteration