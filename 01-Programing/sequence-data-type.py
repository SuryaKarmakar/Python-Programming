# Lists: A list is alterable. You can add and remove items to the list.
list = [1, 2, 3, 4]
list2 = ['surya', 24]

print(type(list))
print('list =', list)
print('list2 =', list2)

# accesss list by index
print(list[2])

list3 = [1, 2, 3, 4]
# insert(position, value)
list3.insert(4, 5)
print('list3 =', list3)

list3.append(6)
print('list3 =', list3)

# pop(position/index)
list3.pop(5)
print('list3 =', list3)