# defining the function
def user_define_function():
    print("This is user define function")

# calling the function
user_define_function()

# function with parameters
def sum(a, b):
    print("Sum of a and b is", a + b)

sum(3, 5)


# function without parameters
def sum2():
    print("Sum of 3 and 2 is", 3 + 2)

sum2()

# function with return statement
def sum3(a, b):
    return a + b

result = sum3(10, 5)
print("Sum of a and b is", result)

# multiple return statement.
def max_number(x, y):
    if x > y:
        return x
    else:
        return y
print(max_number(3, 4))

# call by reference. when a mutable argument are passed into a function and updated into that function then the chnages reflected on actual argument.
lang_list = ["c", "python", "c++"]
def add_more(item):
    lang_list.append(item)
    print(lang_list)

add_more("java")
print(lang_list)

# variable length function.
# we can use * to accept list of parameters as tuple.
def biggest_no(*num):
    print(max(num))

biggest_no(4, 5, 8)
biggest_no(5, 8, 9, 4, 10)

# keyword and variable arguments. order of the passing argument dose't matter. each argument have a unique key.
def activity(name, activity):
    print(name + " is " + activity)

activity(name = "Arya", activity="dancing")
activity(activity="playing", name="Ananya")