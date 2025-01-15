# Implicit Type Conversion: Automatically performed by Python

i = 20
f = 10.11
# here i(int) convert to float automatically by python
print(i + f) 

# Explicit Type Conversion: Manually executed by the programmer

# Converts string to integer
i1 = int('20')
print('i1 =', i1, type(i1)) 

# Converts float to integer
i2 = int(10.11)
print('i2 =', i2, type(i2)) 

# Converts string to float
f1 = float('30')
print('f1 =', f1, type(f1)) 

# Converts integer to string
s1 = str(100)
print('s1 =', s1, type(s1)) 

# Non-zero numbers are converted to True
b1 = bool(0)
b2 = bool('x')
print('b1 =', b1, type(b1))
print('b2 =', b2, type(b2))

# Converts x to list
tuple_to_list = list(('a', 'b', 'c'))
print('tuple_to_list =', tuple_to_list, type(tuple_to_list))

# Converts x to set
list_to_set = set([1, 2, 3, 4])
print('list_to_set =', list_to_set, type(list_to_set))

# Converts x to tuple
list_to_tuple = tuple([1, 2, 3])
print('list_to_tuple =', list_to_tuple, type(list_to_tuple))

# Converts x to dictionary
tuple_to_dict = dict([(1, 'one'), (2, 'two')])
print('tuple_to_dict =', tuple_to_dict, type(tuple_to_dict))