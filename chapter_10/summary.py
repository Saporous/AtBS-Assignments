# Automating the Boring Stuff
# ----------------------------
# Chapter 10 Summary Program
# Objective: Summarize the contents of the chapter in a
# simple and interactive text program
# Summary: learn to use more of the following modules:
# os, shutil, send2trash, zipfile

import os, shutil, send2trash, zipfile
from pathlib import Path
print('''
shutil.copy(source, destination) - copies file from source to destination (strings or Path objects)
    returns a string or Path object of the copied file
shutil.copytree(source, destination) - copies a folder recursively. Returns a string or Path 
    object of the copied directory
shutil.move(source, destination) - movies file or folder from source to destination. Returns
    absolute path of the new location
shutil.rmtree(path) - recursive remove
os.unlink(path) - deletes single file
os.rmdir(path) - deletes single folder. Folder must be empty
send2trash.send2trash(path) - sends file/folder to recycle bin

os.walk(path) - used in for loops: returns 3 values 
    1. (string) current folder name
    2. (list of strings) folder names in the current folder
    3. (list of strings) files in the current folder
Example: 
for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
    print('')

Accessing a zipfile object is similar to accessing a File object with open() and close()
newZip = zipfile.ZipFile(path/file.zip) - opens file.zip. Returns ZipFile object
zipfile.namelist() - returns a list of strings for all files and folders contained inside
zipfile.getinfo(string) - returns ZipInfo object containing information of a single file
ZipInfo.file_size
ZipInfo.compress_size

zipfile.extractall([path]) - extracts zipfile object to cwd or to path parameter. Can create 
    directory if directory does not exist
zipfile.extract(filename,[path]) - extracts single file from zipfile object

newZip = zipfile.ZipFile('new.zip', ['w','a']) - opens ZipFile object in write/append mode
zipfile.write('file.txt', [compress_type=zipfile.ZIP_DEFLATED]) - adds file.txt into new.zip


''')