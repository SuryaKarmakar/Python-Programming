# 1. Lists: A list is alterable/mutable. You can add and remove items to the list.
list1 = [1, 2, 3, 4]
list2 = ['surya', 24]

print(type(list1))
print('list =', list1)
print('list2 =', list2)

# accesss list by index
print(list[2])

list3 = [1, 2, 3, 4]
list4 = ['a', 'b', 'c']
# insert(position, value)
list3.insert(4, 5)
print('insert new data -', list3)

list3.extend(list4)
print('extend list4 to list3 -', list3)

list3.append(6)
print('append new data -', list3)

# pop(position/index)
list3.pop(5)
print('pop data -', list3)

list3.reverse()
print('reverse the list -', list3)

list3.clear()
print('clear all data -', list3)

# 2. Tuples: Tuples are immutable. Values stored in a tuples can't be changed and altered.
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')

print('tuple1 =', tuple1)
print('tuple2 =', tuple2)

# join two tuples together
tuple3 = tuple1 + tuple2
print('tuple3 =', tuple3)

# accesss tuples by index
print(tuple3[1])