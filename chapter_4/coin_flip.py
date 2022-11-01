import random
import time
start_time = time.time()

coinFlip = []
coinFlipCount = 100
numTests = 10000
consecutiveCount = 0

def generateCoinFlipResults(coinFlipCount):
    global coinFlip
    coinFlip = []
    # print('Generating ' + str(coinFlipCount) + ' values...')
    for i in range(coinFlipCount):
        coinFlip.append(random.choice(['T', 'H']))
    # print('Done!')

def searchSixInARow(listOfSix):
    if len(listOfSix) != 6:
        print('List parameter is not 6!')
        return False
    for iter in range(len(listOfSix)):
        if listOfSix[iter] != listOfSix[0]:
            return False
    return True

for i in range(numTests):
    generateCoinFlipResults(coinFlipCount)
    for iter in range(len(coinFlip)-6):
        if searchSixInARow(coinFlip[iter:iter+6]):
            consecutiveCount += 1
            iter += 6
print('After flipping ' + str(coinFlipCount) + ' coins ' + str(numTests) + ' times,')
print('The chance of a 6 streak is ' + str(consecutiveCount/(numTests)) + '%')
print("--- %s seconds ---" % (time.time() - start_time))