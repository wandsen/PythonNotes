import os

if os.path.isdir('Scripts'):
    print("list current directory" , os.listdir())
    fileList = os.listdir('Scripts')
    print (fileList)

