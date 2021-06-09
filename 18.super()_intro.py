'''
- super() is used in a child class to refer to the parent class without explicitly naming it.
- it is used in three contexts:
    (i)accessing parent class properties - especially when same named properties are present in both parent and child classes.
        Ex: in child class use the below code
            super().parent_class_property
    (ii)calling parent class methods - especially when same named methods are present in both parent and child classes.
        Ex: in child class use the below code
            super().parent_class_method
    (iii)Using with initializers
        super() function is used to call the initializer of the parent class from inside of the intializer of the child class.
        
Note:- It's not necessary that the call to super() in a method or in a initializer should be made in the first line of the method.
'''

# Accessing parent properties
'''
class Parent:
    num = 100


class Child(Parent):
    num = 50

    def display(self):
        #accessing parent properties using super()
        print("parent num:",super().num)
        print("child num:",self.num)

obj = Child()
obj.display()
'''

# calling parent class methods using super()
'''
class Parent:
    def display(self):
        print("I am from Parent class")


class Child(Parent):
    def display(self):
        super().display()
        print("I am from Child class)

obj = Child()
obj.display()
'''


class Parent:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Child(Parent):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c


obj = Child(1, 2, 3)
print(obj.a)
print(obj.b)
print(obj.c)
