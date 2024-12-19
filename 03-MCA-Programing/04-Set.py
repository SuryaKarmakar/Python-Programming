# Set: sets are immutable, once a collection of data is stored in a set, it cannot be changed. but you can add new data
# sets are unordered and unindexed, its stored as a random order
# no two sets can have the same value

set1 = {'pencil', 'eraser', 'ruler'}
print('set1 =', set1)

# add new items to a set, you can use the add () function
set1.add("pen")
print('add new value -', set1)

# add the values of one set to another set using the update () function
set2 = {1, 2, 3}
set3 = {'a', 'b', 4}

set2.update(set3)
print('extend set2 with set3 -', set2)

# update () function can be used to add any iterable object such as lists, tuples
list1 = [5, 'x']
tuple1 = (6, 'y')

set2.update(list1, tuple1)
print('extend a tuple to set -', set2)

# remove () or discard () can be used to remove a value from the set
set2.remove('a')
print('remove value -', set2)

# To empty the complete set, you can use the method clear ().
set2.clear()
print('clear all value -', set2)