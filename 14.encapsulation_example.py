'''
- A proper implementation of encapsulation all the properties should be private.
- Any access to the properties from outside of the class would be given by getters and setters.
- So, here GETTERS and SETTERS will provide an INTERFACE to access those private properties
'''


class User:
    def __init__(self, username=None, password=None):
        self.__username = username
        self.__password = password

    def login(self, userName, password):
        if ((self.__username.lower() == userName.lower()) and (self.__password.lower() == password.lower())):
            print("Access granted against username:", self.__username.lower(),
                  " and password:", self.__password.lower())
        else:
            print("Access denied")


rajan = User("rajan", "rajan")
rajan.login("rajan", "rajan")  # login will be successful
rajan.login("rajan", "kumaran")  # login will be failed here
