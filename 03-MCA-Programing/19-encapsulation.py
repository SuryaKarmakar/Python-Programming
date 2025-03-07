class ParentClass:
    def __init__(self):
        self.a = "This is a parent class"
        self._b = "This is a protected member"
        self.__c = "This is a private member"
    
    def print_members(self):
        print("Parent:", self.a) # can access
        print("Parent:", self._b) # can access
        print("Parent:", self.__c) # can access

class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()
        self.print_members()

    def print_child_members(self):
        print("Child:", self.a) # can access
        print("Child:", self._b) # can access
        # AttributeError: 'ChildClass' object has no attribute '_ChildClass__c'
        # print("Child", self.__c) # can't access
    
obj = ChildClass()
obj.print_child_members()