
# Delete the Address key from the nested dictionary.

person = {'Name': 'John', 'Age': 30, 'Address': {'Street': '123 Elm St', 'City': 'Boston'}}

person.popitem() # Will delete last element/attribute Address in place
