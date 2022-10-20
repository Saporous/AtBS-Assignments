# Automating the Boring Stuff
# ----------------------------
# Chapter 1 Summary Program
# Objective: Summarize the contents of the chapter in a simple text program
print('Chapter 1\n')

print('Operators')
print('** exponent: 2**3 = ' + str(2**3))
print('% modulus: 2%3 = ' + str(2%3))
print('// integer division: 22 // 8 = ' + str(22//8))
print('/ division: 22 / 8 = ' + str(22/8))
print('* multiplication: 22 * 8 = ' + str(22*8))
print('- subtraction: 22 - 8 = ' + str(22-8))
print('+ addition: 22 + 8 = ' + str(22+8))
print('')

print('String concatenation')
print('Alice + Bob: ' + 'Alice'+'Bob')
print('String replication')
print('Alice*3: ' + 'Alice'*3)
print('')

print('input() function')
print('test = input(): ')
test = input()
print('')

print('len() function')
print('len(test): ' + str(len(test)))
print('')

print('Text and number equivalence')
print('42 == \'42\': ' + str(42=='42'))
print('42 == 42.0: ' + str(42==42.0))
print('42.0 == 0042.0000: ' + str(42.0 == 0042.0000))