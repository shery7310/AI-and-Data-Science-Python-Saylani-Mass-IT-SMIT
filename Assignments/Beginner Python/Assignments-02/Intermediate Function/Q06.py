# Create a function that accepts a dictionary and returns the key with the highest value.
numbers_dict = {
    "a": 102, "b": 600, "c": 8, "d": 9898, "e": 12, "f": 2332, "g": 732
}
def highest_dict_value(numbers):
    max_value = 0
    values_from_dict = [value for value in numbers_dict.values()] # 102 600 8 9898 12 2332 732
    keys_from_dict = [key for key in numbers_dict.keys()] # "a", "b", "c", "d", "e", "f", "g"
    for index, value in enumerate(values_from_dict):
        temp_index = index + 1
        if temp_index < len(values_from_dict):
            if values_from_dict[index] > values_from_dict[temp_index]:
                temp = values_from_dict[index]
                values_from_dict[index] = values_from_dict[temp_index]
                values_from_dict[temp_index] = temp
        else:
            break
    max_value = values_from_dict[-1]
    for key, value in numbers.items():
        if value == max_value:
            return key


print(f'The key in the current dictionary is "{highest_dict_value(numbers_dict)}"')


