import random
import time
start_time = time.time()

coinFlip = []
coinFlipCount = 100
numTests = 1000
consecutiveCount = 0

def generateCoinFlipResults(coinFlipCount):
    global coinFlip
    coinFlip = []
    # print('Generating ' + str(coinFlipCount) + ' values...')
    for i in range(coinFlipCount):
        coinFlip.append(random.choice(['T', 'H']))
    # print('Done!')

def searchSixInARow(listOfSix, consecutiveValue):
    if len(listOfSix) != 6:
        print('List parameter is not 6!')
        return False
    if listOfSix[0] != consecutiveValue:
        return False
    for iter in range(len(listOfSix)):
        if listOfSix[iter] != listOfSix[0]:
            return False
    return True

for i in range(numTests):
    generateCoinFlipResults(coinFlipCount)
    for iter in range(len(coinFlip)-6):
        if searchSixInARow(coinFlip[iter:iter+6], 'T'):
            consecutiveCount += 1
        if searchSixInARow(coinFlip[iter:iter+6], 'H'):
            consecutiveCount += 1
print('The chance of a 6 streak is ' + str(consecutiveCount/(numTests)) + '%')
print("--- %s seconds ---" % (time.time() - start_time))