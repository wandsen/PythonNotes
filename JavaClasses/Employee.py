class employee:
    perc_raise = 1.05
    
    def __init__(self, first, last, sal):
        self.fname = first
        self.lname = last
        self.sal = sal
        self.email = first + "." + last + '@company.com'

    def fullname(self):
        return "{}{}".format(self.fname, self.lname)
    
    def apply_raise(self):
        self.sal = int(self.sal*1.05)

emp_1 = employee("Alpha", "Jp", 100)
emp_2 = employee("Bravo", "SG", 888)

print("Salary", emp_1.sal)
emp_1.apply_raise()
print("Percentage raise before update", emp_1.perc_raise)

emp_1.perc_raise = 4.5 #modifying the class variable directly
print("Percentage raise after update:", emp_1.perc_raise)

print(emp_1.sal)

