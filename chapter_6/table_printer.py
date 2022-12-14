# Automating the Boring Stuff
# ----------------------------
# Chapter 6 Practice Projects
# Automating the Boring Stuff
# --------------------------------------------------
# Table Printer

# Write a function named printTable() that takes a list of lists of strings 
# and displays it in a well-organized table with each column right-justified. 
# Assume that all the inner lists will contain the same number of strings. 
# For example, the value could look like this:

# tableData = [['apples', 'oranges', 'cherries', 'banana'],
#              ['Alice', 'Bob', 'Carol', 'David'],
#              ['dogs', 'cats', 'moose', 'goose']]

# Your printTable() function would print the following:

#    apples Alice  dogs
#   oranges   Bob  cats
#  cherries Carol moose
#    banana David goose

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(listOflistOfStrings):
    longestWord = []
    for x in range(len(listOflistOfStrings)):
        longestWord.append(0)
        for y in range(len(listOflistOfStrings[0])):
            stringlen = len(listOflistOfStrings[x][y])
            longestWord[x] = stringlen if stringlen > longestWord[x] else longestWord[x]
    for y in range(len(listOflistOfStrings[0])):
        for x in range(len(listOflistOfStrings)):
            print(listOflistOfStrings[x][y].rjust(longestWord[x]+1), end=' ')
        print('')

printTable(tableData)