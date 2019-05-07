import os
import glob

#Find OS name
print('Finding my OS', os.name)

#Get current directory
print("Current working directory", os.getcwd())

#Create a new directory
# os.mkdir('myNewDirectory')

#Listing the directories
print(os.listdir())

#Changing directory
os.chdir('myNewDirectory')
os.chdir('..')

print(os.getcwd())

fileList1 = glob.glob('*.txt')
for i in fileList1:
    print("myfiles" , i)


