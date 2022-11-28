#! python3

# regex_search.py <folder to search> <regex>

# opens all .txt files in a folder and searches for any 
# line that matches a user-supplied regular expression

# Test command:
# python .\regex_search.py .\ '.?\d\d.?'
from pathlib import Path
import os, sys, re

# os.chdir(sys.argv[1])
infilepath = Path.cwd() / sys.argv[1]
if len(sys.argv) == 3:
    regexsearch = re.compile(sys.argv[2])
else:
    print('No regex parameter specified. Exiting')
    exit()
# check if directory is valid
filelist = []
if infilepath.exists():
# get all .txt files in directories
    filelist = list(infilepath.glob('*.txt'))
    print(f'Filelist: {filelist} \n')
else:
    print('Directory does not exist! Exiting')
    exit()
# iterate through all text files and search for regex comparison
for filename in filelist:
    fi = filename.open()
    print(f'Reading {filename}...')
    filecontents = fi.read()
    regresult = regexsearch.findall(filecontents)
    # print found results to terminal
    for iter in range(len(regresult)):
        foundpos = filecontents.find(regresult[iter])
        print(filecontents[foundpos:foundpos+5])