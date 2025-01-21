# Write a function that takes a list and removes all duplicate elements.

nums = input("Enter numbers separated by comma:\n").split(",")
nums = [int(num) for num in nums]
def remove_duplicates(numbers):
    a_set = {nums[0]} # had to add a number to make the dictionary a set
    for num in numbers:
        a_set.add(num)

    return a_set

non_duplicates = remove_duplicates(nums)

# There is another way of doing this we could also have a used a dictionary
# and make the keys the same as values, a python dictionary does not accept
# duplicate keys so only 1 instance of a number in a list would have been kept
print(non_duplicates)
