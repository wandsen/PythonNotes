import shutil, os

#Compressing a file
zipOutputName = "zippedFile"
filetype = 'zip'

path = r"C:\Users\dsen.wan\AppData\Local\Programs\Python\Python37"
fileName= "news.txt"

#Accepts 4 arguments, new zipped file name, the type, the parent path of the file to zip and the name of the file to zip
shutil.make_archive(zipOutputName, filetype, path, fileName)
print("\n\n Done compressing the %s to %s !" %(fileName, zipOutputName))

