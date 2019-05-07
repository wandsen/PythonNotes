import os
import shutil

print("Current directory" , os.getcwd())

#Copying files to another place
def copy_rename(old_file_name, new_file_name, path):
    os.chdir(path)
    src_dir = os.curdir #Requested path will be the current directory
    dst_dir = os.path.join(os.curdir, "subfolder") #Set the destination directory
    src_file = os.path.join(src_dir, old_file_name) #Set destination directory

    shutil.copy(src_file, dst_dir) #copy file from source to destination

#Rename files
def rename(old_file_name, new_file_name, path):
    dst_dir = os.path.join(os.curdir, "subfolder")

    dst_file = os.path.join(dst_dir, old_file_name)
    new_dst_file_name = os.path.join(dst_dir, new_file_name)

    os.rename(dst_file, new_dst_file_name) #rename file

#Moving files to another place
def move(src, dest):
    shutil.move(src, dest)

#UI
userAction = input("What would you like to do \n1) Copy Files\n2) Moving files\n3) Renaming files")
print("useraction" , userAction)
if (userAction == "1"):
    old_file_name = 'testfile2.txt'
    new_file_name = 'newFile2.txt'
    path = '.'
    
    print("Proceeding to copy files from %s to %s" % (path, 'subfolder'))
    copy_rename(old_file_name, new_file_name, path)

elif (userAction == "2"):
    print("moving files")
    src = "testfile2.txt"
    dest = '.\subfolder'
    move(src, dest)

elif (userAction == "3"):
    print('renaming files')
    old_file_name = "testfile2.txt"
    new_file_name = "testfile2Change.txt"
    path = "."
    rename(old_file_name, new_file_name, path)
else:
    print("no such option")


