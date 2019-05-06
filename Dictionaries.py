#Dictionaries

#Creating a dictionary, can be different types
people = {
    'john': 'male',
    'mary': 'female',
    "person": 2
}

#Accessing members in a dictionary
#get is a preffered method as it returns none instead of throwing an error if it does not exist
print(people.get('john'))
print(people['mary'])

#Adding a value into the dictionary
people['Mark'] = "male"
print(people)

#Update entry
people['Mark'] = 'female'
print(people)

#update entry with another object
otherpeople = {
    'john': "apple"
}

people.update(otherpeople)
print('updated people' , people)

#delete entry
del people['Mark']
print(people)

#Built in functions of dictionaries
print('john' in people)
print('john' not in people)

#Return a list of keys from dictionary
print(list(people.keys()))

#Return a list of values in the dictionary
print(list(people.values()))

#Return a list of tuples
listOfTuple = list(people.items())
print(listOfTuple)

#Clear or values of dictionary
people.clear()
print(people)