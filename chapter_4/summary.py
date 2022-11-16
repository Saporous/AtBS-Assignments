# Automating the Boring Stuff
# ----------------------------
# Chapter 4 Summary Program
# Objective: Summarize the contents of the chapter in a
# simple and interactive text program

# Lists
blah = [1, 2, 3, 4]
print('blah = ' + str(blah))

print('Like C, list position starts from 0 and can be indexed')
print('blah[0] = ' + str(blah[0]))

print('Negative index starts from the end')
print('blah[-1] = ' + str(blah[-1]))

print('Lists can be *sliced* with the colon')
print('The first slice parameter defaults to 0 but otherwise denotes the beginning position')
print('The second slice parameter defaults to the size of the list and omits the last indexed item')
print('blah[1:] = ' + str(blah[1:]))

print('len(blah) = ' + str(len(blah)))

test = ['a', 'b', 'c']
print('List concatenation and replication')
print('test = ' + str(test))
print('test + blah = ' + str(test+blah))
print('test * 2 = ' + str(test*2))

print('Removing entries from lists')
del test[1]
print('del test[1] = ' + str(test))

print('*for* looping through lists')
for i in blah:
    print(str(i) + ' ', end='')

print('\n\n*for* looping through lists using range()')
for i in range(len(blah)):
    print(str(blah[i]) + ' ', end='')

print('Search for a value in a list using *in* and *not in*')
print("'a' in test: " + str('a' in test))
print("'z' not in test: " + str('z' not in test))

print('Multiple assignments can be done on lists exactly the same size')
print('test2 = [11, 12, 13, 14]')
test2 = [11, 12, 13, 14]
a, b, c, d = test2
print('a, b, c, d = test2')
print('a = ' + str(a))
print('b = ' + str(b))
print('c = ' + str(c))
print('d = ' + str(d))

print('enumerate() returns an index and object. Combined with tuples it can shorten code')
for index, item in enumerate(test2):
    print('Index: ' + str(index) + ' Item: ' + str(item))

print('the *random* module has random.choice() and random.shuffle()')
import random
print('random.choice(test2): ' + str(random.choice(test2)))
random.shuffle(test2)
print('random.shuffle(test2) : ' + str(test2))

test2 = [11, 12, 13, 14]
print('Find a value in a list using index(). Returns only the first found object')
print('test2.index(12) = ' + str(test2.index(12)))

print('List append() and insert()')
print('test2.append(15): ' + str(test2))
test2.insert(3, 11)
print('test2.insert(3, 11): ' + str(test2))

print('List remove(). Removes only the first found object')
test2.remove(11)
print('test2.remove(11): ' + str(test2))

print('List sort(). Sort by ASCIIbetical by default')
test2.sort()
print('test2.sort(): ' + str(test2))

print('Pass *reverse=True* into sort() to reverse sort')
test2.sort(reverse=True)
print('test2.sort(reverse=True): ' + str(test2))

print('Reverse a list using reverse()')
test2.reverse()
print('test2.reverse(): ' + str(test2))

print('Lists are mutable but strings are immutable')
print('The proper way to modify a string is to use slicing and concatenation')
helloWorld = 'Hello World!'
print('helloWorld = \'Hello World!\'')
newHelloWorld = helloWorld[:5] + ' ' + helloWorld[6:]
print('newHelloWorld = helloWorld[:5] + \' \' + helloWorld[6:]: ' + newHelloWorld)

print('Tuples are similar to immutable lists represented with () parentheses')
print('tuple() and list() can be used to convert between tuples, lists, and strings')

print('id() can dereference an object and identify its address')
print('Python\'s GC deletes an unreferenced varaibles to free memory')

print('copy() and deepcopy() inside the *copy* module can be used to deep copy lists or dicts')
import copy
test = ['A','B','C','D']
print('test = [\'A\',\'B\',\'C\',\'D\']')
test2 = test.copy()
print('test2 = test.copy()')
test2[0] = 'Z'
print('test2[0] = \'Z\'')
print('test: ' + test)
print('test2: ' + test2)


