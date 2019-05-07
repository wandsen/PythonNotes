import os
import shutil
import glob
from pathlib import Path


if os.path.isdir('Scripts'):
    print("list current directory" , os.listdir())
    fileList = os.listdir('Scripts')
    print (fileList)

#Copy file to new file
old = "news.txt"
new = "news2.txt"
shutil.copy(old, new)
print('%s is copied as %s' %(old, new))
list1 = glob.glob('*.txt')
print('list of files', list1)

#Check file exist
print(os.path.exists('news2.txt'))
print(os.path.exists('Lib'))


#Check file exist
file_path = Path(r"C:\Users\dsen.wan\AppData\Local\Programs\Python\Python37\news.txt")
print(file_path.exists())

#Splitting up the path names to access basename, parentname and type
if (file_path.is_file()):
    print("%s is a file" %file_path)
    tup1 = os.path.split(file_path)
    tup2 = os.path.splitext(file_path)

    print("The path of the file is ", tup1[0])
    print("The file is ", tup1[1])
    print("The file type is ", tup2[1])
else:
    print("no such file exist")

#Exception handling
try:
    file_to_open = open(r"C:\Users\dsen.wan\AppData\Local\Programs\Python\Python37\bfile.txt", 'r')
    print('%s found' %file_to_open)
except IOError as e:
    print("Error %s occured" %e)
    print("No such file")

#Using with "WITH AS"
try:
    with open(r"C:\Users\dsen.wan\AppData\Local\Programs\Python\Python37\news.txt", "r", encoding="UTF8") as file:
        for line in file:
            print(line)
except IOError as e:
    print("Error %s occured" %e)
    print("No such file")
