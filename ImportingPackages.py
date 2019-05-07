import random
from turtle import *

space = Screen()
width = space.window_width()
height = space.window_height()

maxX = width/2
minX = -1 * maxX
maxY = height/2
minY = -1 * maxY

jaz = Turtle()
for num in range(10):
    if num % 6 == 0:
        jaz.color('red')
    if num % 9  == 0:
        jaz.color('black')
    randX = random.randrange(minX, maxX)
    randY = random.randrange(minY, maxY)

    jaz.goto(randX, randY)
    jaz.circle(minX)