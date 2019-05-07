#File operations, CRUD, Create, open, work, close

'''
Syntax 
file_object  = open(“filename”, “mode”)

Modes include
'r' - read
'w' - write, files with same name will be replaced
'a' = append, add data to end of file
'r+' = read and write
'''

#Creating a file, if file doesnt exist creates the folder
file_object1 = open("myFile1.txt" , "r+")
file_object1.write("Hello World\n")
file_object1.write("Apple Orange")


#Appending to a file
file_object2 = open("myFile2.txt" , "a")
file_object2.write("Hello ")
file_object2.write("World\n")


#Reading a file
for line in file_object1:
    print('line', line)
file_object1.close()

#Access a word from a file
file_object1 = open("myFile1.txt" , "r+")
for line in file_object1:
    print(line.split())
file_object1.close()

''' note that i closed and open the file in between examples. after the first example
the cursor is already at the end and the second part would not run through anything '''

#Read lines -read everything
file_object1 = open("myFile1.txt" , "r+")
print("Reading lines", file_object1.readlines())
file_object1.close()

