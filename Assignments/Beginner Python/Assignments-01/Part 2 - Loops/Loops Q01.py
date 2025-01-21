# Print numbers from 1 to 20 using a for loop.

for num in range(1, 21):
    print(num, end=" ")

'''
This is the full syntax of print function:
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
Meaing we can pass any number of strings or even variables, by default sep = ' '
and end='\n' if we don't write/specify behaviour of these parameters the print function
automatically adds a space after each string and adds \n after each time the print
statement fully runs. We can overide this by specifiying a value to both or just one of
these parameters.
Default syntax of range function:
range(start, stop, step)
By default the value of start is 0  and step is 1. The range will never provide a
sequence if we do not give an end value. start and stop are optional parameters but in code
I have given value to start so the sequence starts from 1 instead of 0 
Also start is inclusive and end is exclusive meaning the range stops 1 before the given end.
i.e. if we wanted range to end on 20 we would need to give 21.
'''    