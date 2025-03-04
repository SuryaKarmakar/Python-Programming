# returns the number of items(length) in an object.
print(len("hello world"))

# returns largest item.
print(max([1, 2, 3, 4]))

# returns smallest item.
print(max([1, 2, 3, 4]))

# insert value in the string's placeholder.
print("Hello, {}!".format("World")) 

# returns type of the object.
print(type([1, 2, 3, 4]))

# looping iterable and returns a map object.
numbers = [1, 2, 3, 4, 5] 
list(map(lambda x: print(x), numbers))

# filters the given sequence to new filtered sequence.
even_number = list(filter(lambda x: x%2==0, numbers))
print(even_number)