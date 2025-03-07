# Create class: -----------------------------
class Test: # the class keyword is used to create a class.
    pass

# Create object: -----------------------------
# syntax - object_name = class_name(<required arguments>)

class Student:
    name = "surya"
    grade = 8

std = Student()
print("Name:", std.name)
print("Grade:", std.grade)

# Create method: -----------------------------
class Hello:
    def __init__(self):
        pass
    def say_hello(self, name):
        print(f"Hello, {name}")

obj = Hello()
obj.say_hello("John")