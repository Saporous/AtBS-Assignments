# Automating the Boring Stuff
# ----------------------------
# Chapter 3: Zigzag

# This program will create a back-and-forth, zigzag pattern until the user stops it
#  by pressing the Mu editor’s Stop button or by pressing CTRL-C. 
#  When you run this program, the output will look something like this:

#     ********
#    ********
#   ********
#  ********
# ********
#  ********
#   ********
#    ********
#     ********

import time, sys

currentIndent = 0
indentIncreasing = True
maxIndent = 5
minIndent = 0
numStars = 8

try:
    while True:
        print(' ' * currentIndent, end='')
        if indentIncreasing == True:
            if currentIndent >= maxIndent:
                indentIncreasing = False
            elif currentIndent < maxIndent:
                currentIndent = currentIndent + 1
        elif indentIncreasing == False:
            if currentIndent <= minIndent:
                indentIncreasing = True
            elif currentIndent > minIndent:
                currentIndent = currentIndent - 1
        print('*' * numStars)
        time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()