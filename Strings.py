#Characteristics of Strings
myString = "ABCDE"

#Changing Case
lowerCaseString = myString.lower()
print("My lower case string: " , lowerCaseString)

upperCaseString = lowerCaseString.upper()
print("My upper case string: " ,upperCaseString)

#Indexable
print("My string at position 2: " , myString[2])

#Length of String
lengthOfString = len(myString)
print("The length of my String is: ", lengthOfString)

#Covert any type to String
myInt = 123
convertedIntToString = str(myInt)
print("Converted the integer: %d to string: %s" % (myInt, convertedIntToString))

#Remove whitespace at start and end of string
myWhiteSpaceString = " hello John "
cleanString = myWhiteSpaceString.strip()

print("Removed white spaces from statment : " , cleanString)

#Check if string contains certain characters
print(convertedIntToString.isdigit())
print(myString.isalpha())

spaces = "   "
print(spaces.isspace())
print(myString.startswith('A'))
print(myString.endswith('E'))

#Find index of substring
print(myString.find('C'))

#Replace string
print(myString.replace('A','F'))

#Spliting a string, returns an list, note that c is being deleted
mySplitString = myString.split('C')
print(mySplitString)

#Joining a String
print(" ".join(mySplitString))

