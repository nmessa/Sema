#Lab Exercise 11/8/2023 Problem 1
#eratosthenes.py
#Author: nmessa
#Generates a list of prime numbers using Eratosenes algorithm

numbers = []
primeList = []
SIZE = 1000

#initialize the list
for i in range(0, SIZE):
    numbers.append(True)

#execute the sieve
for index in range(2, len(numbers)):
    if numbers[index] == True:
        for i in range(index+1, len(numbers)):
            if i % index == 0:
                numbers[i] = False

#build the list of primes
for i in range(2, len(numbers)):
    if numbers[i] == True:
        primeList.append(i)

print (primeList)
