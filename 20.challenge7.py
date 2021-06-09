class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.balance*self.interestRate/100)


user1 = SavingsAccount("Peter", 6000, 4)
print("Initial balance:", user1.getBalance())
user1.withdrawal(100)
print("Balance after withdrawal:", user1.getBalance())
print("Interest on current balance:", user1.interestAmount())
