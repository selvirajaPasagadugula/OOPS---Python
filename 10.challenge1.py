import math


class Point:
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def sumOfSquareArgs(self):
        print((math.pow(self.arg1, 2)) +
              (math.pow(self.arg2, 2))+(math.pow(self.arg3, 2)))


p1 = Point(10, 20, 30)
p1.sumOfSquareArgs()
