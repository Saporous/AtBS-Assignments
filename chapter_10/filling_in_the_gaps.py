#! python3

# filling_in_the_gaps.py

# finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, 
# in a single folder and locates any gaps in the numbering 
# (such as if there is a spam001.txt and spam003.txt but no spam002.txt). 
# Have the program rename all the later files to close this gap.

# As an added challenge, write another program that can insert gaps 
# into numbered files so that a new file can be added.

# usage: filling_in_the_gaps.py [REMOVE|INSERT] prefix

import os, sys, shutil, re
from pathlib import Path

dir = Path.cwd()
regexresult = []
def identify_files(filename_pattern = 'test'):
    for folderName, subfolders, filenames in os.walk(dir):
        for index, filename in enumerate(filenames):
            result = re.findall(r'(\w+)(\d+)(\..+)', filename)
            if result and result[0][0] == filename_pattern:
                regexresult.append(result)
    print(regexresult)

def fill_missing_files():
    for iter, items in enumerate(regexresult):
        if items[0][1] != iter + 1:
            items[0][1] = iter + 1
    print(regexresult)

def insert_file_space():
    TODO = True

if len(sys.argv) == 3:
    pattern = sys.argv[2]
    if sys.argv[1].lower() == 'remove':
        identify_files() 
        fill_missing_files()
    elif lower(sys.argv[1]) == 'insert':
        insert_file_space()
elif len(sys.argv) >= 1:
    print('filling_in_the_gaps.py [REMOVE|INSERT] prefix')
    exit()