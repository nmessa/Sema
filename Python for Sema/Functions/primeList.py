##primeList.py
##Author: nmessa
##Date: 12.4.2023
##This program prints all prime numbers less than 100

def isPrime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

for number in range(2, 100):
    if isPrime(number):
        print(number, end = " ")

##Output
##2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
