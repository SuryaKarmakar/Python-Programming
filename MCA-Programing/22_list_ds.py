list1 = []
list2 = [1, 2, 3]
list3 = [1, "a", 3.33]
list4 = [1, [1, 2], (2, 3)]

# indexing
print(list2[1])
print(list4[1][1]) # nested indexing
print(list2[-1]) # negative indexing

# slicing. [string_index : end_index]
list5 = [1, 2, 3, 4, 5, 6, 7, 8]
print(list5[3 : 6])

# update list value
update_list = [2, 3, 5]
print("update_list", update_list)
update_list[2] = 4
print("update_list", update_list)

update_list[0 : 3] = [10, 20, 30] # update multiple index using slicing
print("update_list", update_list)

# repetition
print(list2 * 3)

# concatination
print(list2 + list3)

# membership operators
print(1 in list2)
print(2 not in list2)

# iteration
list6 = [1, 2, 3, 4, 5]

# uisng for loop
for x in list6: 
    print(x)

# using loop and range and indexing
length = len(list6)
for x in range(length):
    print(list6[x])

# using while loop
index = 0
while index < length:
    print(list6[index])
    index += 1

# uisng list comprehension
[print(i) for i in list6]

# using enumerate. index and value
list7 = [2, 4, 6, 8, 10]
for index, value in enumerate(list7):
    print(index, "", value)

# calculate length of the list
size = 0
for x in list7:
    size += 1

print(size)

# adding elements using append()
list2.append(4)
print(list2)

# adding multiple elements
list_a = [1, 2, 3]
list_b = [4, 5, 6]

list_a.extend(list_b)
print(list_a)

# adding element in specific index. insert(index, new_element)
list_c = ['a', 'b', 'd', 'e']
list_c.insert(2, 'c')
print(list_c)

# removing elements
del_list = [1, 2, 3, 4, 5, 6, 7, 8]

del del_list[2] # uisng del to remove the element at index 2
print(del_list)

del del_list[1 : 4] # remove index 1 to 3
print(del_list)

del_list.remove(7) # using remove to remove the first occurrence of element 7 
print(del_list)

removed_element = del_list.pop(1) 
print("Removed element:", removed_element) # using pop to remove and return the element at index 1 
print(del_list)

del_list.clear() # remove all elements
print(del_list)