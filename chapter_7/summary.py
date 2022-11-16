# Automating the Boring Stuff
# ----------------------------
# Chapter 7 Summary Program
# Objective: Summarize the contents of the chapter in a
# simple and interactive text program

import re
print('''Regex
compile() takes in a *raw* string and returns a *Regex* object
phoneNumRegex = re.compile(r'\d\d\d*\d\d\d*\d\d\d\d')
search() takes in a string to search when called on a Regex object
and returns a *Match* object
group() is called on a *Match* object to return a string of the matched text
group() can take in an *int* to output different found substrings
Special characters include .  ^  $  *  +  ?  {  }  [  ]  \  |  (  )
They must be escaped with a backslash \\
''')
print(r'''
| the Pipe character matches multiple groups
? the question mark makes the group that precedes it optional
* the star character matches zero or more
+ the plus character maches one or more
{} the curly braces matches a repeat for a specific number of times
{x,y} can also match a range with a minimum *x* and a maximum *y*
{x,y}? overrides the default greedy search with the non-greedy search''')

print('findall() operates on a *Regex* object with an input string')
print('it returns a list of strings')

print(r'''
\d numeric digits 0 to 9
\D inverse \d - any character not digit 0 to 9
\w any letter, numeric digit or _
\W inverse \w
\s any space, tab, or newline character
\S inverse \s''')

print(r'''Custom character classes
re.compile(r'[aeiouAEIOU]')
- hyphen can be used to speicy a range of letter or numbers
^ inverts the character class
''')

print('''
^ the caret character when used at the start of a regex indicates that a match must occur
at the *beginning* of the searched text
$ the dollar character when used at the end of a regex indicates that a match must occur
at the *end* of the searched text
. the dot character is a wildcard character. Combined with a * star will match everything
.* will match everything *except newline*

 The re.compile() function has a second parameter to override the default function actions
re.DOTALL causes the dot character to match EVERYTHING
re.IGNORECASE or re.I will ignore capitalization when passed in re.compile()
re.VERBOSE ignores whitespace and comments inside the string. The triple quote can then be
used to create a multiline string to make the Regex more readable
| the bitwise operator can be used to combine multiple re.compile() parameter 2 options
''')

print(r'''
sub() substitutes new text in place of found patterns when called on a Regex object
Argument 1 is a string to replace *any* matches
Argument 2 is the string for the Regex match
\1 \2 \3 can be used to use the matched text itself for the substitution
''')