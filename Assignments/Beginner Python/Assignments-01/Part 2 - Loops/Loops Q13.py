"""
   *
  ***
 *****
*******
Question: Use nested loops to print a pyramid pattern of *.
3 spaces at start and 3 after the first star, we need to print 1 star
2 spaces at the start for 2nd row of stars, we need to print 3 stars
1 space at the start for 3rd row, we need to print 5 stars
no space in the last row, we need to print 7 stars
Here we printed without use of nested loop
"""

space_count = 3 # in each row number of spaces are getting reduced that's why we need this variable
num = 0 # in each row the number of star is increasing by two from the previous one

for row in range(1, 5): # We need 4 rows so we run this 4 times
    spaces = ' ' * space_count # a new string of spaces is made each time loop restarts
    print(spaces, end="") # in the first iteration 3 spaces are added to the start of stars
                          # and then the end doesn't take the flow to the next line
                          # instead the * in next line of code will start printing from spaces
    print('*' * (row + num)) # in first iteration row = 1 and num = 0 so * is printed 1 time
                             # in the second iteration row = 2 and num = 1, 2 + 1 = 3 so 3 * are printed
    num += 1              # after each print statement value of num increases by 1
    space_count -= 1      # after each print statement value of space_count decreases by 1
print()
# Using Nested Loops

space_count = 3 # we made this to keep track of spaces
count = 0 # this is made to keep track of the extra * in each row for example
          # if row = 2, * is printed two times we add required number of *, it keeps on increasing
for row in range(1, 5):
    for col in range(0,4):
        spaces = ' ' * space_count
        print(spaces, end='')
        print(('*' * row) + ('*' * count) , end="\n")
        count += 1
        break
    space_count -= 1
print()

# better nested logic
# but still we aren't using an internal loop like an internal loop

space_count = 3 # there are 3 spaces at start, this keeps decrementing
spaces = space_count * ' ' # but we later inside the for loop don't use it
# we re allocate a new variable using if condition
for row in range(1, 8, 2):# this stores 1, 3, 5, 7 respectively in row variable
    for col in range(1): # the internal loop will always run 1 time per row i.e. if row = 3, 3 x 1
        if row == 1:
            spaces = ' ' * 3 # spaces keep on decrementing per row
        elif row == 3:
            spaces = ' ' * 2
        elif row == 5:
            spaces = ' ' * 1
        elif row == 7:
            spaces = ' ' * 0
        print(spaces, end="")
        print('*' * row, end="")
        print() # after each set of '*' patterns print along with current space, then we shift to new line

print()

# this is the best logic because it uses separate loop for spaces and separate for *
spaces = 3
for row in range(1, 8, 2): # 1 3 5 7

    # loop for spaces
    for space in range(spaces):
        print(" ", end="")
    spaces -= 1

    # loop for * pattern
    for _ in range(row): # will iterate run 0 to 4 times fetching values 1 3 5 7
                         # as it's an internal loop it will run them times the value in row variable
        print("*", end="") # after each run we override end argument so that flow doesn't go to next line

    print() # to take flow to next line
