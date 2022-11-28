#! python3
# mad_libs.py <infile> [<outfile>]
# reads in a text file passed in via commandline argument
# prompts the user each time the word ADJECTIVE, NOUN, ADVERB, or 
# VERB appears in the text file.
from pathlib import Path
import os

try:
    print(sys.argv[1])
    infile = open(sys.argv[1], 'r')
    infilepath = Path.cwd() / sys.argv[1]
except:
    print('Invalid/no path specified. Program exiting')
    exit()

outfiledir = Path.cwd() / (infilepath.stem + '_output' + infilepath.suffix)
outfile = open(outfiledir, 'a')
filecontents = infile.read().split()

for iter, word in enumerate(filecontents):
    if word == 'ADJECTIVE':
        filecontents[iter] = input('Enter an adjective: ')
    if word == 'NOUN':
        filecontents[iter] = input('Enter an noun: ')
    if word == 'ADVERB':
        filecontents[iter] = input('Enter an adverb: ')
    if word == 'VERB':
        filecontents[iter] = input('Enter an verb: ')
filecontents = ' '.join(filecontents)
print(filecontents)
outfile.write(filecontents)