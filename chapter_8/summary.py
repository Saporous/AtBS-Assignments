# Automating the Boring Stuff
# ----------------------------
# Chapter 8 Summary Program
# Objective: Summarize the contents of the chapter in a
# simple and interactive text program

import pyinputplus as pyip

print(r'''
pyip.inputStr()
pyip.inputNum()
pyip.inputChoice()
pyip.inputMenu()
pyip.inputDatetime()
pyip.inputYesNo()
pyip.inputBool()
pyip.inputEmail()
pyip.inputFilepath()
pyip.inputPassword()

The blank keyword argument permits blank entries
pyip.inputNum(blank=True)

min, max, greaterThan, and lessThan keywords
pyip.inputNum('Enter num: ', min=4)
pyip.inputInt('Enter num: ', greaterThan=4)
pyip.inputFloat('>', min=4, lessThan=6)

Regex can be used or blocked with the allowRegexes/blockRegexes keyword
pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])

timeout, limit, and default keywords
pyip.inputNum(timeout=10, limit=2, default='N/A')
Invalid entries that exceed the keywords will raise a RetryLimitException or TimeoutException

def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' %(sum(numbersList)))
    return int(numbers) # Return an int form of numbers.
    
pyip.inputCustom(addsUpToTen)
''')