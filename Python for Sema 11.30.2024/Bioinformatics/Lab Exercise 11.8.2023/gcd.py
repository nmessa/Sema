#gcd.py
#Author: nmessa
#Find the greatest common divisor of two integers

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

#code to test function
print (gcd(48, 84))
