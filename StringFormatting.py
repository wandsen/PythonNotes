#String formatting using %s
myString = "Hello"
myFloat = 31.00000
myInt = 20

if myString == "Hello":
    print("myString is String: %s" % myString)
if isinstance(myFloat, float) and myFloat == 31.0:
    print("myFloat is Float: %f" % myFloat)
if isinstance(myInt, int) and myInt == 20:
    print("myFloat is Float: %d" % myInt)

#Set the decimals for floats
print("myFloat in 2 decimal points is Float: {:.2f}".format(myFloat))

#Do note that comma is not needed in the print statement
myInt = 123
convertedIntToString = str(myInt)
print("Converted the integer: %d to string: %s" % (myInt, convertedIntToString))

#Formatting using .format
print("My String is: {0}, and my float is {1}".format(myString, myFloat))

#Combining decimals and formatting
origPrice = float(input("Enter the original price"))
discount = float(input("Enter discount percentage: "))
newPrice = (1 - discount/100) * origPrice

print("${1:.2f} discounted by {0:.0f}% is ${2:.2f} ".format(discount, origPrice, newPrice ))

