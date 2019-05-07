import random

#Password Generator
sample = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
password = "".join(random.sample("abcdefghijklmnopquestvwzyz1234567890!@#$%^&", 12))
print(password)

#Reverse a string
def reverseString (string):
    s = ''
    for c in string:
        s = c + s
    return s

print(reverseString("ABCDE"))

#Common element in 2 list
a = [1,1,2,3,5,7,13]
b = [1,2,3]

def findCommon(a, b):
    return print(set(a).intersection(set(b)))

findCommon(a, b)

#Compare random list
c = []
d = []

for x in range(10):
    c.append("".join(random.sample("abcdefghijklmnopquestvwzyz1234567890!@#$%^&", 1)))
    d.append("".join(random.sample("abcdefghijklmnopquestvwzyz1234567890!@#$%^&", 1)))

findCommon(c,d)

#List comprehension for comparison of list
commonNumber = []
[commonNumber.append(x) for x in c for y in d if x == y]
print(commonNumber)