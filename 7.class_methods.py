'''
- Class methods works on class variables and can be accessed using classname
- Class methods can be accessed without creating object
- use @classmethod decorator to declare a method as a class method
- 'cls' is used to refer to the class just like 'self' used to refer to the object
- we can use any other name instead of 'cls' but it's a standard convention
'''


class Animal:
    nature = "Human"

    def __init__(self, name):
        self.name = name

    @classmethod
    def whoAreYou(cls):
        return cls.nature


# me = Animal('Rajan')
# print('called using object',me.whoAreYou())

print('called using classname', Animal.whoAreYou())
