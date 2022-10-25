# Automating the Boring Stuff
# ----------------------------
# Chapter 3: The Collatz Sequence

# Write a function named collatz() that has one parameter named number. 
# If number is even, then collatz() should print number // 2 and return this value. 
# If number is odd, then collatz() should print and return 3 * number + 1.

# Then write a program that lets the user type in an integer and that keeps
# calling collatz() on that number until the function returns the value 1. 

def collatz(number):
    if number % 2:
        val = 3 * number + 1
    else:
        val = number // 2
    print(str(val))
    return val

print('Enter number: ')
num = int(input())

while num != 1:
    num = collatz(num)