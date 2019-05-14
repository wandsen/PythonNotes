import math
from Point import *

class Line:
    def __init__(self, fromPoint, toPoint ):
        self.startPoint = fromPoint
        self.endPoint = toPoint

    def length(self):
        xDiff = self.startPoint.getX() - self.endPoint.getX()
        yDiff = self.startPoint.getY() - self.endPoint.getY()
        return math.sqrt( xDiff * xDiff + yDiff * yDiff )

line1 = Line(pointA, pointB)
print(line1.length())
