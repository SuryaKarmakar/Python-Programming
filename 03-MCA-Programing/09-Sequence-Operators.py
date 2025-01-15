list1 = [1, 2, 3] 
string1 = "Hello" 
tuple1 = (4, 5, 6)

# Use '+' to concatenate two sequences
list2 = list1 + [7, 8, 9] 
print(list2) # list2 = [1, 2, 3, 7, 8, 9]
 
string2 = string1 + " World"
print(string2) # string2 = "Hello World"

tuple2 = tuple1 + (10, 11, 12)
print(tuple2) # tuple2 = (4, 5, 6, 10, 11, 12)

# Use '*' to repeat a sequence a given number of times 
list3 = list1 * 2
print(list3) # list3 = [1, 2, 3, 1, 2, 3]

string3 = string1 * 3
print(string3) # string3 = "HelloHelloHello"

tuple3 = tuple1 * 2
print(tuple3) # tuple3 = (4, 5, 6, 4, 5, 6)

# Use 'in' to check if an element is in a sequence 
print(2 in list1) # True 
print("H" in string1) # True 
print(7 in tuple1) # False

# Use '[]' to access an element by index 
print(list1[0]) # 1 
print(string1[1]) # e 
print(tuple1[2]) # 6 

# Use '[-]' to access an element from the end of the sequence 
print(list1[-1]) # 3 
print(string1[-1]) # o 
print(tuple1[-1]) # 6 