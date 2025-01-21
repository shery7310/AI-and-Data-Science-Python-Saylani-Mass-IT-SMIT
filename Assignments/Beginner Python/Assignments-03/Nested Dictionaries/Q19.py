# Iterate through all the keys in the outermost level of the nested dictionary and print them.
person = {'Name': 'John', 'Age': 30, 'Phone': "123-456-7890", 'Address': {'Street': '123 Elm St', 'City': 'Boston'}}

person.popitem()
for k in person.keys():
    print(person[k])