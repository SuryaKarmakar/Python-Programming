# Write a python program to add and delete key-value pairs in dictionary in different ways.

# Initial dictionary
my_dictionary = {'name': 'John', 'age': 25, 'city': 'New York'}

# Adding key-value pairs using assignment
my_dictionary['occupation'] = 'Engineer'
print(my_dictionary)

# Adding key-value pairs using update() method
new_data = {'salary': 60000, 'hobbies': ['reading', 'coding']}
my_dictionary.update(new_data)
print(my_dictionary)

# Deleting a key-value pair using del keyword
if 'age' in my_dictionary:
    del my_dictionary['age']
print(my_dictionary)

# Deleting a key-value pair using pop() method
removed_value = my_dictionary.pop('hobbies', None)  # None is the default value if key is not found
print(f"Removed Value: {removed_value}")
print(my_dictionary)

# Deleting the last item using popitem() method
removed_item = my_dictionary.popitem()
print(f"Removed Item: {removed_item}")
print(my_dictionary)