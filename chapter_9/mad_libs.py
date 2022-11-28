#! python3

# mad_libs.py <infile> [<outfile>]

# reads in a text file passed in via commandline argument
# prompts the user each time the word ADJECTIVE, NOUN, ADVERB, or 
# VERB appears in the text file.

# Test command:
# echo blue chair kicked door | python .\mad_libs.py mad_libs.txt

from pathlib import Path
import os, sys, re

fn = sys.argv[1]
checkdir = Path(sys.argv[1])
if checkdir.exists():
    infile = open(sys.argv[1], 'r')
else:
    print('File does not exist! Exiting')
    exit()

if len(sys.argv) == 2:
    outfiledir = os.getcwd() + '\\' + fn[:fn.find('.')] + '_output' + fn[fn.find('.'):]
elif len(sys.argv) == 3:
    outfiledir = Path.cwd() / sys.argv[2]

outfile = open(outfiledir, 'a')
print(outfiledir)
# filecontents = infile.read().split
filecontents = infile.read()
filecontentssplit = []
compiledresult = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
searchresult = compiledresult.findall(filecontents)

for iter, word in enumerate(searchresult):
    userinput = input('Enter a(n) ' + searchresult[iter] + ': ')
    filecontents = compiledresult.sub(userinput, filecontents, 1)
        
print(filecontents)
outfile.write(filecontents)