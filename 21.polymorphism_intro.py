'''
Polymorphism = poly(many) + morph(form)
- In OOPs, polymorphism refers to the same object exhibiting different forms and behaviours.
- This can be acheived using:(i)methods (ii)inheritance

In polymorphism using Inheritance
- Base class declares a function without providing it's implementation
- Each derived class inherits the function declaration and provides it's own implementation
- So that the developer doesn't have to remember the specific names of each function
'''

'''
# Polymorphism using methods


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    def getArea(self):
        return self.width * self.height


class Circle:
    def __init__(self, radius=0):
        self.radius = radius
        self.sides = 0

    def getArea(self):
        return 3.142*(self.radius*self.radius)


shapes = [Rectangle(2, 3), Circle(10)]
print("No.of sides for a Rectangle is: ", shapes[0].sides)
print("Area of Rectangle is: ", shapes[0].getArea())
print("No.of sides for a Circle is: ", shapes[1].sides)
print("Area of Circle is: ", shapes[1].getArea())
'''


# Polymorphism using Inheritance
class Shape:
    def __init__(self):
        self.side = 0

    def getArea(self):
        pass


class Rectangle(Shape):
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    def getArea(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius=0):
        self.radius = radius
        self.sides = 0

    def getArea(self):
        return 3.142*(self.radius*self.radius)


shapes = [Rectangle(2, 3), Circle(10)]
print("Area of Rectangle:", shapes[0].getArea())
print("Area of Square:", shapes[1].getArea())
