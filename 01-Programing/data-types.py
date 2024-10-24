# 1. Strings: strings are immutable.
str1 = 'hello'
str2 = "world"
str3 = "type's"
print(type(str1))
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

# 2. Numbers: numbers are immutable.
# Integers
i = 10 
i2 = int(10) 
print(type(i), type(2))
print('i =', i, 'i2 =', i2)

# Floating Point Numbers
f = 10.00
f2 = float(10.00)
print(type(f), type(f2))
print('f =', f, 'f2 =', f2)

# Complex Numbers
c = 7 + 4j
print(type(c))
print('c =', c)

# extract only the imaginary or real part of the complex number
c2 = 44.9 + 89e4j 
print ('real =', c2.real) 
print ('imaginary =', c2.imag)