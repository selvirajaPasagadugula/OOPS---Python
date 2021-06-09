'''
- Method ovrerriding is the process of redefining the parent class's method in child class
- Method ovrerriding requires presence of Inheritance 
'''


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
