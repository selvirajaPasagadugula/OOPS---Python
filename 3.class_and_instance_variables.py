'''
Class variable - shared variables that are common to all the instances of a class. Change in them will affect the all objects instances
Instance variable - these are unique to each instance. Change in them will affect only that specific instance
'''


class India:
    country = 'India'  # Class variable

    def __init__(self, name):  # Instance variable
        self.name = name


class Pakistan:
    country = 'Pakistan'  # Class variable

    def __init__(self, name):  # Instance variable
        self.name = name


kl_rahul = India('KL Rahul')
rohit = India('Rohit')
print(kl_rahul.country)
print(kl_rahul.name)
print(rohit.country)
print(rohit.name)
print()
babar_azam = Pakistan('Babar Azam')
inzamam = Pakistan('Inzamam')
print(babar_azam.country)
print(babar_azam.name)
print(inzamam.country)
print(inzamam.name)
print()

# The class variables can also be accessed by using class name
print(India.country)
print(Pakistan.country)
