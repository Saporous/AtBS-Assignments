# Automating the Boring Stuff
# ----------------------------
# Chapter 6 Summary Program
# Objective: Summarize the contents of the chapter in a
# simple and interactive text program

print('''Strings can single or double quotes to encapsulate text
Common escape characters include: \\t Tab, \\n Newline, \\" double quote, and \\ backslash
print(r\'') add the r for a "raw string" which considers backslash as a normal character

print(\'\'\'blah
blah
blah\'\'\') 
Multiline strings are denoted with triple quotes
Multiline quotes also do not need escape characters for single and double quotes
# Hash character is used to denote single lime comments

""" Triple double quotes open and close a multiline comment

Strings share functionality with lists for *slicing*, *in*, and *not in* operators
''')
print(r'String interpolation makes use of the % operator which saves usage of the str() function')
print('''Python 3.6 introduced f-strings which use {} braces as an alternative to string interpolation

String Methods
upper() and lower() return a string with all letters converted to uppercase or lowercase, respectively
isupper() and islower() returns Boolean if the string has >= 1 letter and all letters are uppercase or lowercase respectively
isalpha() only letters, isalnum() only letters and numbers, isdecimal() only num
isspace() only spaces, tabs, and newlines, istitle() only words that begin with uppercase
startswith() and endswith() returns True if begins or ends with the string

join() accepts a list of strings and combines them, separated by the string the function is called on
print('ABC'.join(['Hello', 'there', 'user'])'
''')
print('ABC'.join(['Hello', 'there', 'user']))
print('''split() is called on a string and by default splits using whitespace as a delimiter. A string
may be passed in as a custom delimiter
\'MyABCnameABCisABCJeff\'.split(\'AB\')''')
print('MyABCnameABCisABCJeff'.split('AB'))

print('''partition() is called on a string and takes in a string separator. It returns a tuple of the
string contents before, the first instance of of the separator, and everything after the separator
print('Hello, world'.partition('w'))''')
print('Hello, world'.partition('w'))
print('''Multiple assignment can be handy to one-line the returned tuple
separator = 'w'
before, separator, after = 'Hello, world'.partition(separator)
print(before+after)''')
separator = 'w'
before, separator, after = 'Hello, world'.partition(separator)
print(before+after)

print('''Text Formatting
rjust(), ljust(), center() are called on a string and return a padded version of the string
The default second parameter is whitespace but can be replaced with any character

strip(), rstrip(), and lstrip() are called on a string and return a string without whitespace at
the beginning, end, or both

ord(), chr() convert to and from Unicode
''')