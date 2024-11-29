#simulation.py
#Author: nmessa
#Lab Exercise 11.6.2023
#Runs a simulation of three trials of one million coin flips and
#one million dice rolls

import random
rollTally = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
flipTally = {'H':0, 'T':0}
rollTotal = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
flipTotal = {'H':0, 'T':0}

def flipCoin():
    rNumber = random.random()
    if rNumber > 0.5:
        return 'H'
    else:
        return 'T'

def rollDice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

def flipSim(n):
    result = []
    for i in range(n):
        result.append(flipCoin())
    return result

def rollSim(n):
    result = []
    for i in range(n):
        result.append(rollDice())
    return result

def calcMean(X):
    return sum(X) / len(X)

def printHistogram(X):
    print()
    print ("Histogram")
    keyList = list(X.keys())
    maxValue = 0
    for e in keyList:
        if X[e] > maxValue:
            maxValue = X[e]
    scaleFactor = 40.0 / maxValue
    for e in keyList:
        X[e] *= scaleFactor
    for e in keyList:
        X[e] = int(X[e])
    vals = list(X.values())
    for i in range(len(vals)):
        print (keyList[i], "  ", end = '')
        for i in range(vals[i]):
            print ("X", end = '')
        print()
    print()
    print()

        
def  runSimulation(function, n, numTrials, simDict , totalDict):
    for trial in range(1, numTrials+1):
        dict = simDict.copy()               #reset the dictionary counts to 0
        print ("Trial", trial)
        answer = function(n)                #roll or flip n times
        for e in answer:
            dict[e] += 1                           #add up the values for each outcome
        print (dict)
        keyList = list(dict.keys())
        for e in keyList:
            totalDict[e] += dict[e]         #add values to totalDict
    print()
    #Calculate average of numTrials trials
    for e in keyList:
        totalDict[e] /= float(numTrials)
    #Round the values in the dictionary
    for e in keyList:
        totalDict[e] = round(totalDict[e], 2)
    #Print the rounded average
    print ("Average = ", totalDict)
    printHistogram(totalDict)

print ('Running coin flip simulation .....')
runSimulation(flipSim, 1000000, 3, flipTally, flipTotal)
print()
print()
print ('Running dice roll simulation .....')
runSimulation(rollSim, 1000000, 3, rollTally, rollTotal)
        
    
        
    
