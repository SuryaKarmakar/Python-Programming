# Number Variable: Variables that are used to save number values are numeric variables.
# integers
num = 20 
print("num =", num)

# floating-point numbers
floatNum = 26.90 
print("floatNum =",floatNum)

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
def localFunc():
    localVar = "Local Variables"
    print("localVar =", localVar)
localFunc()

# Global Variables:
globalVar = "Global Variables"
def globalFunc():
    print("globalVar from local scope", globalVar)
globalFunc()
print("globalVar from global scope", globalVar)

# Update global variable from local scope:
newVal = 10
def updateFunc():
    global newVal
    newVal = 20
updateFunc()
print(newVal)

# Delete A Variable:
delMe = "delete me"
print("delMe =", delMe)
del delMe
# NameError: name 'delMe' is not defined
# print(delMe) 