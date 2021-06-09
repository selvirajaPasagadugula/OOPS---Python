'''
- Inheritance provides a way to create a new class from an existing class.
- The new class will be a specialised version of the existing class such that it inherits all the non-private properties and methods of the existing class.
- Where there is "IS A" relationship we can use Inheritance.
- "Object" class is the base class of all the classes in Python.
- Whenever a class gets created, it is by default becomes the subclass of the "Object" class.
'''

'''
- PARENT/SUPER/BASE class allows the reuse of it's public properties in another class.
- CHILD/SUB/DERIVED class is the one that inherits or extends the superclass.
'''

'''
Types of Inheritance:
    1.Single
    2.Multi-level
    3.Hierarchical
    4.Multiple
    5.Hybrid(Multiple + Multi-level)

Advantages of Inheritance:
    1.Code re-usability
    2.Code modification
    3.Extensibility
    4.Data hiding
'''


class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        # calling constructor of the parent class
        Vehicle.__init__(self, make, color, model)
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print("Doors:", self.doors)


obj1 = Car("Suzuki", "Grey", 2015, 4)
obj1.printCarDetails()
