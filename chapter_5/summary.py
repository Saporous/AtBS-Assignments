# Automating the Boring Stuff
# ----------------------------
# Chapter 5 Summary Program
# Objective: Summarize the contents of the chapter in a
# simple and interactive text program

print('Dictionaries and Structuring Data')

print('\nDictionaries are filled with key-value pairs')
print('They are constructed with braces {}')
print('Python dictionaries are unsorted and have no "first" item')
print('Note: Python 3.7+ dictionaries remember insertion order')
print('\nUse keys(), values(), and items() methods to access a dictionary')
print('These functions return list-like values of data type dict_keys, dict_values, and dict_items')

print('test = {\'color\':\'red\', \'smell\':\'yummy\'}')
test = {'color':'red', 'smell':'yummy'}
for index, (key, value) in enumerate(test.items()):
    print(str(index) + ': ' + key + ':' + value)

print('\n Tip: The list-like data type dict_items can be turned into an actual list using list()')
print('list(test.items())')
print(list(test.items()))

print('\nUse *in* or *not in* to check if a key or value exists in a dict')
print('\'color\' in test.keys() = ' + str('color' in test.keys()))

print('\nget() takes a key and returns its value. The second parameter is returned\
in case the key does not exist')
print('test.get(\'smell\', \'NONE\') = ' + test.get('smell', 'NONE'))
print('test.get(\'hair\', \'NONE\') = ' + test.get('hair', 'NONE'))

print('\nsetdefault() condenses an empty value check followed by an assignment into a function')
if 'nose' not in test:
    test['nose'] = 'long'
    print(test['nose'])
print('The first parameter is the key to check - if the key has a value it will be returned')
print('The second parameter is the value to set IF the key does not exist')
print('test.setdefault(\'nose\', \'long\'): ' + test.setdefault('nose', 'long'))

print('\nThe pprint module (pretty print) introduces functions used to print out dict contents')
import pprint
count = {}
for iter in test.keys():
    for char in range(len(iter)):
        count.setdefault(iter[char], 0)
        count[iter[char]] += 1
print('Compare print() to pprint(). Note that pprint sorts the keys')
print('print(count): ', end='')
print(count)
print('pprint.pprint(count): ', end='')
pprint.pprint(count)
print('Use pformat() for variable assignment. The following code should print the same value as before')
print('print(\'pprint.pformat(count)\'): ' + pprint.pformat(count))
