# Number Variable: Variables that are used to save number values are numeric variables.
# integers
num = 20 
print("num =", num)

# floating-point numbers
float_num = 26.90 
print("float_num =",float_num)

# complex numbers
cpx = 3 + 4j 
print("cpx =", cpx)

# String Variable: Strings are a sequence of characters.
str1 = 'String 1'
str2 = "String 2" 
print("str1 =", str1)
print("str2 =", str2)

# Multiple Assignment: 
# You can assign one value to several variables at the same time.
a = b = c = 1
print("a =", a, "b =", b, "c =", c)

# You can also assign different values to different variables in the same command.
d, e, f = 2, 3, 4
print("d =", d, "e =", e, "f =", f)

# Local Variables:
def local_func():
    local_var = "Local Variables"
    print("local_var =", local_var)
local_func()

# Global Variables:
global_var = "Global Variables"
def global_func():
    print("global_var from local scope", global_var)
global_func()
print("global_var from global scope", global_var)

# Update global variable from local scope:
new_val = 10
def update_func():
    global new_val
    new_val = 20
update_func()
print(new_val)

# Delete A Variable:
del_me = "delete me"
print("del_me =", del_me)
del del_me
# NameError: name 'del_me' is not defined
# print(del_me) 