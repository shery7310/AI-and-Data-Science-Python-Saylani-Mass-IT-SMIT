# Write a program to print the first 10 Fibonacci numbers.
# these are the first 10:
# 1 1 2 3 5 8 13 21 34 55

li = [1, 1]

count = 0
for num in range(1, 9):
    li.append(li[count]+li[num])
    count += 1

'''
We used list so we don't have to make logic up for the first two ones we already have
in the list. List datastructure is used because it has functions such as append or insert
to insert values being created by for loop
List values can be changed in place
'''