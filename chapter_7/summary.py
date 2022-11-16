# Automating the Boring Stuff
# ----------------------------
# Chapter 7 Summary Program
# Objective: Summarize the contents of the chapter in a
# simple and interactive text program

import re
print('Regex')
print('compile() takes in a *raw* string and returns a *Regex* object')
phoneNumRegex = re.compile(r'\d\d\d*\d\d\d*\d\d\d\d')
print('search() takes in a string to search when called on a Regex object \
and returns a *Match* object')
print('group() is called on a *Match* object to return a string of the matched text')
print('group() can take in an *int* to output different found substrings')

print('Special characters include .  ^  $  *  +  ?  {  }  [  ]  \  |  (  )')
print('They must be escaped with a backslash \\')

print(r'''
| the Pipe character matches multiple groups
? the question mark makes the group that precedes it optional
* the star character matches zero or more
+ the plus character maches one or more
'{} the curly braces matches a repeat for a specific number of times
'{x,y} can also match a range with a minimum *x* and a maximum *y*
{x,y}? overrides the default greedy search with the non-greedy search''')

print('findall() ')