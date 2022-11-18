# Chapter 8
# multiplication_quiz.py

import random, time

numQuestions = 10
numCorrect = 0
numAttemptsAllowed = 3

for questions in range(numQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    timeBegin = time.time()
    attempts = 0
    while True:
        if attempts >= 3:
            print('Out of tries!')
            break
        answer = input('%s * %s = ' %(num1, num2))
        if time.time() - timeBegin >= 8.0:
            print('Out of time!')
            time.sleep(1)
            break
        if int(answer) != num1*num2:
            print('Incorrect, try again.')
            attempts += 1
            continue
        else: 
            numCorrect += 1
            print('Correct!')
            time.sleep(1)
            break

time.sleep(1)
print('Score: %s / %s' %(numCorrect, numQuestions))