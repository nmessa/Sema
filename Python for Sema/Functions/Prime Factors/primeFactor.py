#Prime Factorization Program
#Author: nmessa

def isPrime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def factor(number):
    factors = []
    if isPrime(number):     #need to handle the case of a number is prime
        factors.append(number)
        return factors
    for i in range(2, number):
        while number % i == 0:
            factors.append(i)
            number /= i
    return factors
    
number = int(input("Enter a number you want factored: "))
print ("The prime factors are: " + str(factor(number)))
