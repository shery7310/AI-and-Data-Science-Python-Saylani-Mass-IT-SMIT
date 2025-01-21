#!/bin/bash
# I used this to create 30 Python Files that were needed to complete dictionaries assignment
# Check for Fish shell and inform user
if [[ $SHELL != *fish ]]; then
    echo "This script assumes you are using Fish shell. Continuing anyway..."
fi

# Define the problem statements
read -r -d '' problems << 'EOF'
# Create a dictionary student with keys: name, age, and grade. Assign them appropriate values.
# Access the value of the key grade in the student dictionary.
# Add a new key city to the student dictionary and set its value to "New York".
# Update the value of the age key in the student dictionary to 20.
# Remove the key city from the student dictionary.
# Iterate through the dictionary student and print all keys.
# Iterate through the dictionary student and print all values.
# Iterate through the dictionary student and print all key-value pairs in the format key: value.
# Check if the key grade exists in the student dictionary and print True or False.
# Count the total number of keys in the student dictionary.
# Merge the following two dictionaries and print the result: dict1 = {'a': 1, 'b': 2}, dict2 = {'c': 3, 'd': 4}.
# Create a dictionary from a list of tuples: [('name', 'Alice'), ('age', 25), ('city', 'Paris')].
# Sort the keys of the dictionary {'z': 1, 'a': 2, 'c': 3} in ascending order and print the sorted dictionary.
# Reverse the dictionary {'a': 1, 'b': 2, 'c': 3} so that keys become values and values become keys.
# Write a Python function to check if two dictionaries are identical (contain the same key-value pairs).
# Create a nested dictionary to represent: Person: Name: John, Age: 30, Address: Street: 123 Elm St, City: Boston.
# Access the value of the city key in the nested dictionary from the previous question.
# Add a new key Phone to the nested dictionary with the value "123-456-7890".
# Delete the Address key from the nested dictionary.
# Iterate through all the keys in the outermost level of the nested dictionary and print them.
# Use a dictionary to count the occurrences of each word in the string: "hello world hello python world".
# Write a Python program to find the key with the maximum value in the dictionary: {'a': 10, 'b': 15, 'c': 7}.
# Create a dictionary to map numbers 1 to 5 to their squares (e.g., {1: 1, 2: 4, 3: 9, ...}).
# Write a Python program to remove duplicate values from the dictionary: {'a': 10, 'b': 15, 'c': 10, 'd': 15}.
# Write a Python function that accepts a dictionary and a key, and returns the value associated with the key. If the key doesn’t exist, return "Key not found".
# Given two dictionaries dict1 = {'a': 5, 'b': 10} and dict2 = {'a': 3, 'b': 7}, write a Python program to add the values of matching keys and print the result.
# Write a Python program to create a dictionary where the keys are the first n positive integers, and the values are their cubes. Take n as user input.
# Flatten the following nested dictionary into a single-level dictionary: {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}.
# Write a Python program to split a dictionary into two dictionaries based on whether the values are odd or even.
# Create a dictionary comprehension to filter out all keys in {'a': 1, 'b': 2, 'c': 3, 'd': 4} where the value is less than 3.
EOF

# Split problem statements into an array
IFS=$'\n' read -r -d '' -a problem_array <<< "$problems"

# Create .py files and add the respective problem statement
for i in $(seq -w 1 30); do
    filename="Q$i.py"
    echo "${problem_array[$((10#$i - 1))]}" > "$filename"
    echo "Created $filename"
done

echo "All files created successfully!"

