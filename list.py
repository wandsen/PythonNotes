#List in python

#Methods modify original list

#Declare a list
colors = [1,2,3]
print(colors[1])

#Add a value at the end
colors.append(4)
print(colors)

#Add element in a specific index, first argument is the index where the value will go
colors.insert(1, 100)
print(colors) 

#Add list of elements at the end
colors.extend([101,102])

#Removing element
colors.remove(1)
print(colors)

#Remove and return element, argument takes in the index
returnedElement = colors.pop(1)
print(returnedElement)