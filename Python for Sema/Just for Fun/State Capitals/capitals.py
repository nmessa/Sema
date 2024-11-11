#capitals.py
#Author: nmessa
#State capital drill program

import random

#read in data from external file
infile = open('state_capitals.txt', 'r')
data = infile.readlines()
infile.close()

#create data structures to hold data for program
data2 = []  #clean data
stateCaps = {}  #dictionary for state:capital key:value pairs
score = 0       #initialize score count
numStates = 50


#remove the newLines (\n) from each data element
for element in range(len(data) - 1):
    index = data[element].find('\n')
    data2.append(data[element][0:index])
data2.append(data[-1]) #add last data element to the clean list

#build the state:capital dictionary
for i in range(0, len(data) - 1, 2):
    stateCaps[data2[i]] = data2[i+1]

#create a list to randomly choose from
states = list(stateCaps.keys())

#Generate 10 drill problems
for i in range(10):
    rNumber = random.randint(0, numStates - 1)
    answer = input("What is the capital of " + states[rNumber] + '? ')
    if answer == stateCaps[states[rNumber]]:    #test for correct answer
        score += 1
        
    else:
        print ("Wrong the correct answer is", stateCaps[states[rNumber]])
    states.remove(states[rNumber])  #remove the state from the possible queries
    numStates -= 1
        
print (score/10.0 * 100)          #print percentage correct



