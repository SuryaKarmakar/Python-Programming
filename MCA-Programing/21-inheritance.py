# Inheritance: ----------------------
class ParentClass():
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_name(self):
        print(self.name)
    
    def get_id(self):
        print(self.id)
    
class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()
    
    obj = ParentClass("John", 101)
    obj.get_name()
    obj.get_id()

# Single Inheritance: ----------------------
# The attributes of a single parent class are passed on to the child class.
class Animal:  # parent class
    def __init__(self, name):  # name parameter added
        self.name = name  # assigning name to the instance
    
    def speak(self):
        pass

class Dog(Animal):  # child class inheriting from Animal
    def __init__(self, name):  # name parameter added
        super().__init__(name)  # passing name to the parent class constructor
        
    def speak(self):
        return f"{self.name} says woof"
    

# creating an instance of Dog
dog = Dog("Buddy")
print(dog.speak())

# Multiple Inheritance: ----------------------
class Father:
    def skils(self):
        print("Gardening", "Programming")

class Mother:
    def skils(self):
        print("Cooking", "Art")

class Child(Father, Mother): # Child class inheriting from both Father and Mother class
    def skils(self):
        Father.skils(self)
        Mother.skils(self)
        print("Sports")

# creating as instance of Child
child = Child()
child.skils()

# Multilevel Inheritance: ----------------------
class Grandfather: 
    def height(self): 
        print("Height is 6 feet")

class Father(Grandfather):  # Inherits from Grandfather 
    def personality(self): 
        print("Great personality") 
        
class Son(Father):  # Inherits from Father 
    def skills(self): 
        print("Excellent in studies") 

# creating an instance of Son 
son = Son() 
son.height()  # From Grandfather 
son.personality()  # From Father 
son.skills()  # From Son itself 

# Hierarchical Inheritance: ----------------------
class Vehicle: 
    def general_usage(self): 
        print("General use: Transportation") 

class Car(Vehicle):  # Inherits from Vehicle 
    def specific_usage(self): 
        print("Specific use: Drive to work") 

class Truck(Vehicle):  # Inherits from Vehicle 
    def specific_usage(self): 
        print("Specific use: Transport goods") 

car = Car() 
truck = Truck() 
car.general_usage()  # From Vehicle 
car.specific_usage()  # From Car 
truck.general_usage()  # From Vehicle 
truck.specific_usage()  # From Truck 

# Hybrid Inheritance: ----------------------
class School: 
    def function1(self): 
        print("This function is in school.")

class Teacher1(School): 
    def function2(self): 
        print("This function is in teacher 1.") 

class Teacher2(School): 
    def function3(self): 
        print("This function is in teacher 2.")

class Student(Teacher1, Teacher2): 
    def function4(self): 
        print("This function is in student.")

# Creating an instance of Student 
student = Student() 
student.function1()  # From School 
student.function2()  # From Teacher1 
student.function3()  # From Teacher2 
student.function4()  # From Student itself 