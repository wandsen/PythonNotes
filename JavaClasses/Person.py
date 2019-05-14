class Person:
    def __init__(self, f, l, a):
        self.firstname = f
        self.lastname = l
        self.age = a

    def __str__(self):
        return "[Person:" + self.firstname + " " + self.lastname + "(" + str(self.age) + ")]"

class Account:
    def __init__(self, person, num):
        self.holder = person
        self.num = num
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
    def __str__(self):
        return self.holder.firstname + self.holder.lastname

anne = Person("Anne", "Friedrich", 85)
anneAcc = Account(anne, 1)
print(anne, anneAcc)