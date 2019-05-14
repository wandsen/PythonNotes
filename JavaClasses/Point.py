class Point:
    def __init__(self, x = 0, y = 0):
        self.xCoord = x
        self.yCoord = y

    def __str__(self):
        return "(" + str( self.xCoord) + "," + str(self.yCoord) + ")"
    
    def getX(self):
        return self.xCoord
    
    def getY(self):
        return self.yCoord
    
    def shift(self, xInc, yInc):
        self.xCoord += xInc
        self.yCoord += yInc

pointA = Point(5, 7)
pointB = Point()

print(pointA)
print(pointB)
