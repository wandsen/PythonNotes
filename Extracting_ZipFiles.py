import os, shutil
from zipfile import ZipFile

#Extracting stuff from zipped file
path = r"C:\Users\dsen.wan\AppData\Local\Programs\Python\Python37"
os.chdir(path)
file_name = 'zippedFile.zip'

with ZipFile(file_name, 'r') as zip:
    zip.printdir()
    print('\n\n Extracting the text now')
    zip.extractall()
    print('\n\n Done extracting the %s' %file_name)