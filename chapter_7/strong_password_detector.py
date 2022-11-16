"""Strong Password Detection

Write a function that uses regular expressions to make sure the password 
string it is passed is strong. A strong password is defined as one that 
is at least eight characters long, contains both uppercase and lowercase 
characters, and has at least one digit. You may need to test the string 
against multiple regex patterns to validate its strength.
"""

import re

passwordList = [
    '1234',
    'abcd',
    '12345678',
    'abcd12348',
    'ABCDEDFGST',
    'AbCdedfasdf',
    '1234567',
    'asdfqwer',
    'aahsijdb1',
    '123ASDFASD',
    'asdfQ12dasd',
    'ThisV4lidPassword']

def isStrongPassword(pw):
    hasNumber = re.compile(r'\d+')
    hasLower = re.compile(r'[a-z]')
    hasUpper = re.compile(r'[A-Z]')
    if len(pw) < 8:
        return False
    if hasNumber.search(pw) is None:
        return False
    if hasLower.search(pw) is None:
        return False
    if hasUpper.search(pw) is None:
        return False
    return True

for password in passwordList:
    print(str(isStrongPassword(password)))