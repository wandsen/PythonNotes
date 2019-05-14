from abc import ABC, abstractmethod

class Person():
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def __str__(self):
        return "I am " + self.firstName + " " + self.lastName

class Account(ABC):
    
    def __init__(self, num, holder):
        print("Creating Account")
        self.num = num
        self.holder = holder
        self.__balance = 0

    @abstractmethod
    def deposit(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    def getBalance(self):
        return self.__balance
    
    def setBalance(self, amount):
        self.__balance = amount

    def __str__(self):
        return "This account belongs to " + self.holder.firstName + self.holder.lastName


class SavingsAccount(Account):
    interestRate = 0.05

    def apply_interest(self):
        self.getbalance = self.getBalance() * interestRate

    def deposit(self, amount):
        print("executing deposit", amount)
        self.setBalance(self.getBalance() + amount)

    def withdraw(self, amount):
        self.setBalance(self.getBalance() - amount)


class CheckingAccount(Account):
    __creditRange = 2000

    def __init__(self, num, holder, credit_range):
        print("Creating checking account")
        self.__creditRange = credit_range
        self.num = num
        self.holder = holder

    def deposit(self, amount):
        self.__creditRange -= amount

    def withdraw(self, amount):
        self.__creditRange += amount

    def getCreditRange(self):
        return self.__creditRange


John = Person("John", "Doe", 29)
print(John)

JohnSavingAccount = SavingsAccount(1, John)
print(JohnSavingAccount)


#Try deposit money in savings account
print(JohnSavingAccount.getBalance())
JohnSavingAccount.deposit(20)
print(JohnSavingAccount.getBalance())

#Checking account
JohnCheckingAccount = CheckingAccount(1, "John", 0)
print("John checking account credit range is: ", JohnCheckingAccount.getCreditRange())

#Try withdrawing from checking account
JohnCheckingAccount.withdraw(100)
print(JohnCheckingAccount.getCreditRange())

