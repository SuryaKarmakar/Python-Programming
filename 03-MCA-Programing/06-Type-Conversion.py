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
tupleToList = list(('a', 'b', 'c'))
print('tupleToList =', tupleToList, type(tupleToList))

# Converts x to set
listToSet = set([1, 2, 3, 4])
print('listToSet =', listToSet, type(listToSet))

# Converts x to tuple
listTuple = tuple([1, 2, 3])
print('listTuple =', listTuple, type(listTuple))

# Converts x to dictionary
tupleToDict = dict([(1, 'one'), (2, 'two')])
print('tupleToDict =', tupleToDict, type(tupleToDict))