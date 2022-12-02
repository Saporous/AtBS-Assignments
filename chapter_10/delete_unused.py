#! python3

# delete_unused.py

# walks through a folder tree and searches for exceptionally
# large files or folders—say, ones that have a file size of 
# more than 100MB. (Remember that to get a file’s size, you 
# can use os.path.getsize() from the os module.) 
# Print these files with their absolute path to the screen.

# usage: delete_unused.py [directory]

import os, sys, shutil
from pathlib import Path

dir = Path.cwd()
if len(sys.argv) > 1:
    if sys.argv[1] == '-h' or sys.argv[1] == '-H':
        print('delete_unused.py [directory]')
        exit()
    if not Path.exists(sys.argv[1]):
        print('invalid directory')
        exit()
    else: dir = sys.argv[1]


for folderName, subfolders, filenames in os.walk(dir):
    for filename in filenames:
        if os.path.getsize(filename) > 100000000:
            print(Path.cwd()/filename)
