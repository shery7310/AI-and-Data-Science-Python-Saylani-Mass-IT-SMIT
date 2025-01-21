# Create a nested dictionary to represent: Person: Name: John, Age: 30, Address:
# Street: 123 Elm St, City: Boston.
# Access the value of the City

person = {'Name': 'John', 'Age': 30, 'Address': {'Street': '123 Elm St', 'City': 'Boston'}}

print(person['Address']['City'])