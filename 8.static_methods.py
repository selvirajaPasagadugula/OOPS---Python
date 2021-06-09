'''
- static methods are usually limited to their class only and not their objects.
- used as utility functions inside the class (OR) when we don't want the inherited classes to modify a method definition
- just like the class methods, static methods can be accessed both by class name and object name
- it doesn't use any reference to the object or class. So, no need of 'self' or 'cls'

- static methods don't know anything about the state of the class i.e., they cannot modify the class attributes
- the purpose of it is to use it's parameters and produce a useful result
'''


class BodyInfo:
    @staticmethod
    def bmi(weight, height):
        return weight/(height**2)


weight = 75
height = 1.8
print(BodyInfo.bmi(weight, height))
