#overloading the operator function, limited to only the object

class My2Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return My2Vector(self.x + other.x, self.y + other.y)

v1 = My2Vector(1,2)
v2 = My2Vector(3,4)

v3 = v1 + v2 #the __add__ method is overloaded
print(v3.x, v3.y)