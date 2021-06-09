class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return (self.__width * self.__length)

    def perimeter(self):
        return 2*(self.__width + self.__length)


rect1 = Rectangle(1, 2)
rect2 = Rectangle(5, 10)
print("Reactagle1 Area:", rect1.area())
print("Reactagle1 Perimeter:", rect1.perimeter())
print("Reactagle2 Area:", rect2.area())
print("Reactagle2 Perimeter:", rect2.perimeter())
