"""
Flattening a list of lists is a process of transforming a two-Dimensional list into a One-Dimensional
list by un-nesting every list element kept in the list of lists, that is, transforming
[[9, 8, 7], [6, 5, 4], [3, 2, 1]] to [9, 8, 7, 6, 5, 4, 3, 2, 1].
According to www.javatpoint.com/flatten-list-in-python
Write a function to flatten a nested list.
"""
from build.lib.setuptools.namespaces import flatten

a_list = [[10, 20, 30, 40], [50, 60, 70], [80, 90]]
'''
Some more lists we can check this against:
[[9, 8, 7], [6, 5, 4], [3, 2, 1]]
[[10, 20, 30, 40], [50, 60, 70], [80, 90, 100]]
[[10, 20, 30, 40], [50, 60, 70], [80, 90]]  
'''

def flatten_li(nums):
    flattened_li = []
    for li_elem in a_list:
        for elem in li_elem:
            flattened_li.append(elem)
    return flattened_li

    # This can also be done using a list comprehension

print(f"The flattened list is {flatten_li(a_list)}")