add_number = lambda a, b: a + b
print(add_number(3, 5))

# lambda function with map function.
numbers = [1, 2, 3, 4, 5]
square = list(map(lambda x: x**2, numbers))
print(square)