#! python3
# selective_copy.py
# walks through a folder tree and searches for files with 
# a specified file extension (such as .pdf or .jpg). 
# Copies found  files from whatever location they are in to a new folder.

# usage: selective_copy.py extension new_folder_name
# usage example: python .\selective_copy.py .txt \test

import os, sys, shutil, re

if len(sys.argv) < 3:
    print('''
    selective_copy.py extension_regex new_folder_name
    ''')
    exit()

regex = re.compile(sys.argv[1])
destinationfolder = os.getcwd() + str(sys.argv[2])
if not os.path.exists(destinationfolder):
    os.makedirs(destinationfolder)

for folderName, subfolders, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        regresult = regex.findall(filename)
        if regresult:
            print(f'Copying {filename} to {destinationfolder}\{filename}')
            shutil.copy(filename, destinationfolder + '\\' + str(filename))