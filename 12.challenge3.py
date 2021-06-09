class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return (self.num1+self.num2)

    def subtract(self):
        return self.num1-self.num2

    def multiply(self):
        return self.num1*self.num2

    def divide(self):
        return self.num1/self.num2


demo = Calculator(70, 20)
print("Addition:", demo.add())
print("Subtraction:", demo.subtract())
print("Multiplication:", demo.multiply())
print("Division:", demo.divide())
