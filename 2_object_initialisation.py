#can we create speacial methods in Python. If yes How? if no... Why..?
class Employee:
        def __init__(self,id,name,salary,department):
                self.id = id
                self.name = name
                self.salary = salary
                self.department = department

Seetha = Employee('234','seetha',34000,'Human Resources')
print(Seetha)
print(Seetha.id)
print(Seetha.name)
print(Seetha.salary)
print(Seetha.department)

'''
#Object creation with default parameters
class Employee:
        def __init__(self,id='Xu9e2Sw0i',name=None,salary=0,department=None):
                self.id = id
                self.name = name
                self.salary = salary
                self.department = department

anonymous = Employee()
rajan = Employee('890','Rajan',45000,'Developer')

print('Anonymous:\nanonymous.id\nanonymous.name\nanonymous.salary\nanonymous.department)
print('Rajan:\nrajan.id\nrajan.name\nrajan.salary\nrajan.department')
'''