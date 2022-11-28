# Automating the Boring Stuff
# ----------------------------
# Chapter 9 Summary Program
# Objective: Summarize the contents of the chapter in a
# simple and interactive text program
from pathlib import Path
print('''
Chapter 9 - Reading and Writing Files

Don't forget:
Windows and MacOS directories are not case sensitive. Linux directories are.
MacOS and Linux paths use forward slashes / while Windows uses backslashes \\

The pathlib module was introduced in Python 3.4 to replace older os.path functions
For legacy Python 2 versions use the pathlib2 module

Path objects can be concatenated using the / operator
Path('spam') / 'bacon' / 'eggs'

Path.cwd() get current working directory
os.getcwd() equivalent
os.path.abspath('.') get current working directory

os.chdir() change directory

Path.home() get user home directory
print(os.path.expanduser('~'))

Path('C:\\Users\\Al\\spam').mkdir() create directory
os.makedirs() 

Attributes of a Path object
Path.is_absolute returns true or false if the Path object is an absolute directory
Path.anchor returns the root folder (ex: C:\\)
Path.parent returns the folder that contains the file
Path.name returns the filename including extension
Path.sufix returns the file extension
Path.drive returns the storage device letter (in windows)
Path.parents returns a Path list accessible with index entry for each parent folder

os.path equivalences
os.path.basename(calcFilePath) returns string equivalent to Path.name
os.path.dirname(calcFilePath) returns string equivalent to Path.parent
os.path.split() returns a string tuple of parent directory and base name
instead, string split(os.sep) can be used to split a path string into a list of strings

os.path.getsize(path) returns the size of a file
os.listdir(path) returns a list of directories

Glob Patterns
Path.cwd().glob('*') generates Path of objects matching a search term
list.Path.cwd().glob('*') turns it into a list
* matches any string
? matches a single character

Path Validation
Path.exists() returns True if the path exists
Path.is_file() returns True if the path exists AND is a file
Path.is_dir() returns True if the path exists AND is a directory

Path CAN be used to open and write files but it is discouraged
Path.write_text() creates and overwrites a text file
Path.read_text() reads the contents of a file

open(path, [r,w,a]) open a file with read, write, or append
read() returns a string with the entire contents of a file
readlines() returns a list of strings one string for each line of text
write() 
close()
''')