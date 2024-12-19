# Dictionary: dictionary is mutable
# data stored in pair of key: value
# dictionary are stored in order

dict1 = {
    'name': 'surya',
    'age': 24,
    'isMale': True
}
print('dict1 =', dict1)

# To return the value of a specific key
print('name =', dict1['name'])
print('age =', dict1.get('age'))

# To get a list of the keys included in a dictionary 
print('keys =', dict1.keys())

# To get a list of values present in the dictionary
print('values =', dict1.values())

# To update the dictionary by adding key:value pairs
dict1.update({'age': 25})
print('add/update new element -', dict1)

dict1.update({'address': 'xyz'})
print('dict1 =', dict1)

# To remove the element of the specified key
dict1.pop('address')
print('dict1 =', dict1)

# To remove all the elements of a dictionary
dict1.clear()
print('remove all elements -', dict1)