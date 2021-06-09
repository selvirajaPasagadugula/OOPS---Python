'''
Method overloading:
- memory efficient(saves memory) code can be written so that program can be compiled faster
- keeps code clean, minimal and understandable
- implements the feature of OOPs "Polymorphism"
- polymorphism is a way of making a function accept objects of different classes if they behave similarly

- method overloading can also be achieved through default arguments as we can have with and without sending enough arguments
'''


class Square:
    side = 5

    def calculate_area(self):
        return self.side * self.side


class Triangle:
    base = 5
    height = 4

    def calculate_area(self):
        return 0.5 * self.base * self.height


sq = Square()
tri = Triangle()
print("Area of square: ", sq.calculate_area())
print("Area of triangle: ", tri.calculate_area())

# The below two ways will also works where we have used
# (i)a loop to iterate through the objects and
# (ii)a function to which we passed objects to

'''
for obj in (sq, tri):
    print(obj.calculate_area())
'''

'''
find_area_of_shape(obj):
    obj.calculate_area()

find_area_of_shape(sq)
find_area_of_shape(tri)
'''
