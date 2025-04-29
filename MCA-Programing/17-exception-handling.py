# # Name Error: --------------------------

# # 1. When the variable or function name is misspelt.
# books = ["Sherlock Homes", "The Order", "The Alchemist"]
# print(boooks) # NameError: name 'boooks' is not defined

# # 2. When a function is called before it is declared.
# books = ["Sherlock Homes", "The Order", "The Alchemist"]
# get_books(books) # NameError: name 'get_books' is not defined

# def get_books():
#     for x in books:
#         print(x)

# # 3. When we have not defined a variable.
# print(book) # NameError: name 'book' is not defined
# book = "Sherlock Homes"

# # 4. When a string is not defined properly.
# print(Hello) # NameError: name 'Hello' is not defined

# # 5. When a variable is declared out of scope.
# def programming_books():
#     p_books = ["java", "python", "c++"]
#     print(p_books)

# print(p_books) # NameError: name 'p_books' is not defined

# #  Indentation Error: --------------------------
# age = 18
# if age > 18:
# print("Age is greater than 18") # IndentationError: expected an indented block after 'if' statement
# else:
# print("Age is less than 18")

# # IO Error: --------------------------
# file = open("file.txt", "r") # FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'
# contents = file.readline()
# print(contents)
# file.close()

# Try Except Statement: --------------------------

import sys 

randomList = ['a', 0, 2]

for entry in randomList: 
    try: 
        print("The entry is", entry) 
        r = 1/int(entry) 
        break 
    except: 
        print("Oops!", sys.exc_info()[0], "occurred.") 
        print("Next entry.") 
        print() 

print("The reciprcal of", entry, "is", r)

# Try Except Else Statement: --------------------------
try:
    num = int(input("Enter a number: "))
    result = 1/num
except:
    print("Oops!", sys.exc_info()[0], "occurred.") 
else:
    # if no error arise in try block then else block will execute.
    print(result) 

# Multiple Exceptions: --------------------------
try:
    num = int(input("Enter a number: "))
    result = 1/num
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Division By 0 Not Allowed")

# Multiple Exceptions In Single Line: --------------------------
try:
    num = int(input("Enter a number: "))
    result = 1/num
except (ValueError, ZeroDivisionError) as e:
    print(e)

# Try and Finally Block: --------------------------
try:
    file = open("README.md", "r")
except FileExistsError:
    print("File not found")
finally:
    print("closing the file")
    file.close()

# Raising Exceptions: --------------------------
# we can manually raise exceptions by using the raise keyword.
try:  
    a = int(input("Enter a positive integer: "))  
    if a <= 0:  
        raise ValueError("Not a positive number!") # raising the ValueError exception
    else:
        print(a) 
except ValueError as ve:  
    print(ve) 

# Custom Exceptions: --------------------------
# programmer can create their own custom exceptions deriving Exception class.
class ValueToSmallError(Exception):
    pass
class ValueToLargeError(Exception):
    pass

number = 10
try:
    i_num = int(input("Enter a number: "))
    if i_num > number:
        raise ValueToLargeError
    else:
        raise ValueToSmallError
except ValueToSmallError:
    print("This value is too small")
except ValueToLargeError:
    print("This value is too large")