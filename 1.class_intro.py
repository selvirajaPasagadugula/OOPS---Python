#Initializing the properties of the class is necessary, without them program will not compile successfully.

'''
#Assigning values while defining class
class Employee:
        ID = 12345
        salary = 24000
        department = "Human Resources"

raghavan = Employee()
print(raghavan.ID,'\t',raghavan.salary,'\t',raghavan.department)
'''


#Creating the properties outside the class
class Employee:
        ID = 12345
        salary = 24000
        department = "Human Resources"

kumaran = Employee()
kumaran.title = "Manager"
print(kumaran.ID,'\t',kumaran.salary,'\t',kumaran.department,'\t',kumaran.title)
