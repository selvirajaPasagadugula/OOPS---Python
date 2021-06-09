# We are asked not to use initializers and to use setters to do the job
class Student:
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getRollNumber(self):
        return self.__rollNumber

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

stu1 = Student()
stu1.setName("Raman")
stu1.setRollNumber(836)
print(stu1.getName())
print(stu1.getRollNumber())