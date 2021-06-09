'''
- data hiding can be divided into two main components: (i) encapsulation (ii)abstraction
- encapsulation refers to binding data and methods to manipulate that data as a single unit(Class) 
- a good convention is to keep all the variables as private in a class to restrict direct access by 
  other classes and implementing "public methods" to let outside world communicate with this class
- these methods are called "SETTERS" and "GETTERS"
- we can also implement other custom methods
'''

# A getter method allows reading a property's value
# A setter method allows modifying a property value
# ***IMPORTANT: It is a common convention to write the name of the corresponding
# member field with the name of the get or set method
# Ex: getUsername(),setUsername()


class User:
    def __init__(self, username=None):
        self.__username = username

    def getUsername(self):
        return self.__username

    def setUsername(self, newUserName):
        self.__username = newUserName


user1 = User("Rajan")
print("before setting:", user1.getUsername())
user1.setUsername("Kumaran")
print("after setting:", user1.getUsername())
