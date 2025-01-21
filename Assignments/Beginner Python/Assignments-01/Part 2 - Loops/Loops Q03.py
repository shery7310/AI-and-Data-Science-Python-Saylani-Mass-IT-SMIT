# Write a program to calculate the sum of all numbers between 1 and 100.
# By between here we mean from 2 to 99

counter = 2
sum = 0

while counter < 100:
    sum += counter
    counter += 1
print(sum)

# counter is iterating over numbers i.e. 2, 3, 4, 5 ..... 99
# sum is adding previous value with current count value
# i.e. for 1st iteration sum = 0 + 2, then for 2nd iteration
# sum = 2 + 3, then for 3rd iteration sum = 5 + 4
# here the second value is the counter value and the first one
# being added is the previous value stored in some value