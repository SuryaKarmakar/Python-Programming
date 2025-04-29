# create set
set1 = set() # creating a empty set
set2 = {1, 2, 3, 4, 5}
set3 = {1, 2, "a", "b", (1, 2, 3)}

# creating string to set
set4 = set("Python") 
print(set4)

# creating tuple to set
set5 = set((1, 2, 3, 4))
print(set5)

# creating list to set
set6 = set([1, 2, 3])
print(set6)

# add elements
set1.add(1)
print(set1)

# add tupple to a set
tuple1 = (2, 3, 4)
set1.add(tuple1)
print(set1)

# update element
set_a = {1, 2, 3}
set_b = {"a", "b", "c"}

set_b.update("d")
print(set_b)
set_b.update(set_a)
print(set_b)

set_b.update([1.11, 2.22])
print(set_b)

# discard element
set2.discard(1)
print(set2)

set2.discard(10)
print(set2)

print(set2.discard(2))
print(set2)