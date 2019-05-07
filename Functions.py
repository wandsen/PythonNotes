#Notes on functions

#Creating a functions


#Variable length arguments
def myVariableArgs (*argv):
    for arg in argv:
        print(arg)
myVariableArgs("hello", "world")

#Recursion
def myRecursion(n):
    if n <= 1:
        return 1
    else:
        fact = n * myRecursion(n-1)
        return fact
#print(myRecursion(3))

#Fibonnanci Sequence
def fibonnanci(n):
    if n <= 1:
        return 1
    else: 
        result = fibonnanci(n-1) + fibonnanci(n-2)
        return result

nterms = 10
for i in range(nterms):
    print(fibonnanci(i))

