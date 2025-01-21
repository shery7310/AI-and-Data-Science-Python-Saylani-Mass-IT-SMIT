# Create a function that takes a list of numbers and returns the largest number.

def is_largest():
    index_0, index_1, temp = 0, 1, 0
    count = 1
    nums = input("Enter Any Numbers separated by a comma and a space example: 2, 3, 4, 5:\n").split(", ")
    nums = [int(num) for num in nums] # list comprehension to convert the list of string into a list of integers


    for index_num in range(len(nums) + 1): # this runs to loop 1 more time than length of nums list
                                           # We run this one more time so value of index_1 reaches the 1 more than the length
                                           # as soon index_1 > len(nums) the internal while loops stops running
        while index_1 < len(nums):         # in each iteration previous two values are compared and if first of those values is greater
                                           # then those values are swapped if not then they are not swapped
            count += 1 # to count the iterations it took to make the largest number reach the end of the loop
            # 22, 3, 41, 5, 7, 9, 11, 21, 1
            if nums[index_0] > nums[index_1]:
                temp = nums[index_0] # as we replace value at nums[index_0] we need to store it temporarily and then pass it to nums[index_1]
                nums[index_0] = nums[index_1] # here value at nums[index_1] is stored into nums[index_0]
                nums[index_1] = temp # here ORIGINAL value at nums[index_0] is stored into nums[index_1] using temp variable


            index_0 += 1 # to create a sliding window without usage of another nested loop we use both these variables
            index_1 += 1
    print("The iteration ran:",count,"times")

    return nums[-1] # the largest number reaches the end

print(f"{is_largest()} is the largest number in the list passed")

'''
Here are some inputs this can be checked against:
22, 3, 41, 5, 7, 9, 11, 21, 1
13, 27, 35, 4, 8, 10, 19, 23, 2
6, 18, 29, 31, 3, 15, 20, 14, 8
12, 25, 7, 2, 33, 11, 9, 5, 17
30, 21, 1, 16, 28, 24, 19, 13, 4
'''