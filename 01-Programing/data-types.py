# Strings: strings are immutable. once declared and assigned a value, they cannot be changed
str1 = 'hello'
str2 = "world"
str3 = "type's"
print("str1 =", str1, "str2 =", str2, "str3 =", str3)

# use triple quotes for multiple line (it's a alternative of \n)
str4 = '''I will learn Python. 
I want to learn to code.'''
print(str4)

# find the length of the string
print(len(str1))

# access substring from a string
print(str1[1])

# slice a substring
print(str1[0:2])