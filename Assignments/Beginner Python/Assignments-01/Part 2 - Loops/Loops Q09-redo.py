''' 0 1 1 2 3 5 8 13 21 34 55
Some People say that Fibonacci Series starts with 0 and some say it starts with 1.
We are going to start it with 1
Each Next number is the sum of previous/preceding 2 numbers
In this implementation I am using for loop to print fibonacci series
there is no need to use list but i am using it so we actually see how varaible sum is being created
in each iteration.
'''

a, b = 0, 1
for i in range(9):
    sum = a + b # 1 2 3 5 8 13 21 34 55
    a = b  # 1 1 2 3 5 8 13 21 34
    print(a, end=" ") # 1 1 2 3 5 8 13 21 34 55
    b = sum

