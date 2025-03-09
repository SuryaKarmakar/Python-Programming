# creating tuple
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ("a", "b", "c", "d", "e")
tuple3 = (1, 2, 3, "a", "b", "c", 1.11, 2.22, 3.33) # tuple with mixed data types
tuple4 = 1, "a", 1.11 # tuple without parenthess
tuple5 = (1, 1, 2, 2) # tuple with duplicate values
tuple6 = ((1, 2, 3), ["a", "b", "c"]) # nested tuple

# indexing
print(tuple1[1])
print(tuple6[0][1])

# slicing. (start_index : end_index)
print(tuple1[0 : 3])

# negative indexing
print(tuple1[-1])

# delete tuple
try:
    del tuple1
    print(tuple1)
except NameError:
    print("NameError")

# addition of 2 tuple
print(tuple2 + tuple5)

# multiplication
print(tuple5 * 3)

# membership operator
print("a" in tuple2)
print("x" not in tuple2)

# min and max
print(min(tuple2))
print(max(tuple2))

# iteration (we can use all loops)
for x in tuple2:
    print(x)