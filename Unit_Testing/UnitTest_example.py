def recursion_factorial(n):
    if (n ==1):
        return n
    else:
        return n * recursion_factorial(n-1)

def addition():
    return 5 + 5

n = 7
print('Factorial of %s' %n, recursion_factorial(n))
print(addition())