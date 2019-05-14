class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    @property #this function is chosen to be overloaded
    def gotmarks(self):
        return self.name + ' obtained ' + self.marks + 'marks'

    @gotmarks.setter #this is the overloaded function, note that @gotmarks has to be the same name as the function tagged with @property
    def gotmarks(self, sentence):
        name, rand, marks = sentence.split(' ')
        self.name = name
        self.marks = marks
    
    @property
    def total(self):
        return self.name + self.marks

    @total.getter
    def total(self):
        if self.marks*2 > 50:
            return 'Pass' + self.name


st = Student("rena", "25")
print(st.gotmarks)
st.gotmarks = "Gazel obtained 42" #the rand is not used in this case
print(st.gotmark)
