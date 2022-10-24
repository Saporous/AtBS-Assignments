# Automating the Boring Stuff
# ----------------------------
# Chapter 2 Summary Program
# Objective: Summarize the contents of the chapter in a
# simple and interactive text program

print('Boolean Comparison Operators')
print('==, !=, >, >=, <, <= will return True or False (note capitalization')
print('1 == True: ' + str(1==True))
print('1 != False: ' + str(1==False))
print('True == False' + str(True==False))
blah = 42
print('blah = 42, blah == 42.0: ' + str(blah==42.0))

print('\nBinary Boolean Operators')
print('and, and or operators take in two Boolean values')
print('True and True: ' + str(True and True))
print('True or False: ' + str(True or False))

print('\nnot returns one operator inverted')
print('not True: ' + str(not True))

print('\nBlocks of Code: Python is whitespace sensitive')
print('Blocks begin when the indentation increases')
print("Blocks end when the indentation decreases to zero or to a containing block’s indentation.")

print('\nFlow Control: if, elif, else')
age = 5
if age == 5:
    print(age)

print('\nwhile Loop Statements')
i = 0
while i < 10:
    print(i)
    i = i + 2
    continue

print('\nan equilvanet for loop statement')
for j in range(0, 10, 2):
    print(j)

print('\nrange() can take 1-3 parameters. range(start, end, step)')

print('\nusing modules: import [module]')
import random
for i in range(5):
    print(random.randint(1,10))

print('\nfrom import Statements')
print('imports the module and creates references to all public objects defined by the module')
print("basically, the module's objects can be directly called inside the program")
from random import *
print(randint(1,10))

print('\nround() function: ')
print('Converts float to int and rounds up or down')
print('round(5.9): ' + str(round(5.9)))
print('round(5.1): ' + str(round(5.1)))

print('\nabs() function: ')
print('Outputs the absolute value of an input float or int')
print('abs(-1.1): ' + str(abs(-1.1)))
print('abs(-1): ' + str(abs(-1)))