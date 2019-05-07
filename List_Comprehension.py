#List comprehension - returns a list
numbers = [1,2]
squares = []

for n in numbers:
    squares.append(n**2)

anotherSquare = [n**2 for n in numbers]
print(anotherSquare)

#Using conditions in list comprehensions
list_a = [1,2,3,4]
list_b = [1,2,6,8]

common_num = []

for a in list_a:
    for b in list_b:
        if a == b:
            common_num.append(a)
print(common_num)

anotherCommon_Num = [a for a in list_a for b in list_b if a == b]
print("another common", anotherCommon_Num)
#note that the first a is the return value when it meets the last condition

