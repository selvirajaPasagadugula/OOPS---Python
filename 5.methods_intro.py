'''
- In python methods are of three types: 
    1.Instance methods 
    2.Class methods 
    3.Static methods
- Always 'self' is the first parameter for instance methods in python
- return statement is optional
- the visual difference between methods and functions in python is the first argument(self) in method definition
- 'self' can be replaced with any name but it's a standaard convention to use 'self'
- if the user doesn't use 'self' then the first argument will be used for reference to the object

'''


class Employee:
    def __init__(self, id=None, name="None", salary=None, department=None):
        self.id = id
        self.name = name
        self.salary = salary
        self.department = department

    def tax(self):
        return self.salary*.2

    def salaryPerday(self):
        return self.salary/30


emp1 = Employee("567", "Jacob", 30000, "Dev-Ops")

print("Details of Steve:")
print("ID:", emp1.id)
print("Name:", emp1.name)
print("Salary:", emp1.salary)
print("Department:", emp1.department)
print("Tax paying:", emp1.tax())
print("Salary per day:", emp1.salaryPerday())
