'''
- by default, all the properties and methods of a class are public i.e., they can be accessed from any where in the program.
- public attributes are accessible throught the program i.e., inside and outside of the class.
- private attributes are accessible only inside the class(not even accessible through the object created from class)
- private attributes can be made by using double underscores(__) as prefix
- 
'''

# How about the "protected" members


class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # private variable

    def displaySalary(self):  # public method
        print("Salary:", self.__salary)

    def __displayID(self):  # private method
        print("ID", self.ID)


steve = Employee(3456, 70000)
print(steve.displaySalary())
# print(steve.__displayID()) ##This will generate an error
print(steve._Employee__displayID())  # This doesn't give error
