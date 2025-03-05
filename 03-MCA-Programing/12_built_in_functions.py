import time
from datetime import date
from datetime import datetime

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

# Date and Time Functions ----------------------------

# returns the number of seconds passed after epoch.
print(time.time())

# convert the number of seconds elapsed since epoch and returns the value in local time using the function struct_time().
print(time.localtime())

# convert the tuple returned from localtime() functions to string form.
print(time.asctime())

# halting execution of a program for 5 sec.
# time.sleep(5)

# creating date object with day, month and year. here datetime is a class and date is the constructor.
date = date(2025, 5, 20)
print(date)

# get current date.
today = date.today()
print(today)

# comparison of 2 dates.
x = datetime(2025, 2, 15)
y = datetime(2025, 2, 10)
print(x > y)
print(x < y)
print(datetime(2025, 1, 1) == datetime(2025, 1, 1))

#  Miscellaneous Functions ----------------------------

# returns absolute value of the given number.
print(abs(-20.20))
print(abs(-20))

# its return True if all the elements are True, otherwise return False.
list1 = [1, 2, 3]
list2 = [1, 2, 0]
print(all(list1))
print(all(list2))

# converts decimal number to binary number.
print(bin(1))

# return a boolean value or converts the given value to a boolean value.
print(bool("hello"))
print(bool(1))
print(bool({}))

# converting data types using its coding schemes.
str = "Python is the best"
x = bytes(str, 'utf-8') 
print (x)

# returns the boolean value TRUE if the argument appears callable and FALSE if it does not.
def function():
    print("function")
fucn = function
print(callable(fucn))

num = 10
print(callable(num))

# convert source code to executable object.
x = 20
exe_obj = compile("x", "test", "single")
exec(exe_obj)

# returns sum of the elements in sequence.
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))

# its return True if any of the elements are True, if all the elements are False then return False.
list3 = [0, 0, 1, 0]
print(any(list3))