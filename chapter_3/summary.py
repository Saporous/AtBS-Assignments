# Automating the Boring Stuff
# ----------------------------
# Chapter 3 Summary Program
# Objective: Summarize the contents of the chapter in a
# simple and interactive text program

def myFunc(arg1, arg2 = 0):
    print(arg1)
    print(arg2)

# Define, Call, Pass, Argument, Parameter
# Function definition starts with *def*
# To call the function is to execute it
# Calling a function may require passing an argument
# The function definition may contain parameters that arguments will pass variables through

# Return Values and Return Statements
# A *return* statement consists of the *return* keyword and a value or expression to return

# The None Value
print('\nThe None Value')
# *None* is a unique reserved keyword with type NoneType
# *None* is the default return value for functions without a return statement
blah = print("asdf")
print("None == blah: " + str(None == blah))

# print() Keyword Arguments 
# end='\n'
print('Hello', end='')
print('World')
# sep = ''
print('a', 'b', 'c', sep=',')

# Local and Global Scope
print('\nLocal and Global Scope')
# Global variables can be read from local scope as long as it is defined before execution
blah2 = "blah2"
def modBlah():
    print(blah2)

modBlah()

def globBlah():
    global blah2
    blah2 = "modBlah"

print(blah2)

# Exception handling
print('\nException Handling')
# Programs default to the *try:* code block. If an error occurs it immediately begins
# execution of the *except:* code block
try:
    print(42/21)
    print(42/0)
    print(42/42)
except ZeroDivisionError:
    print("Error: Invalid argument")

print("Exception complete")