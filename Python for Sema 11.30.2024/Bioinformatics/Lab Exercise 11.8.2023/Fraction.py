#Lab Exercise 11/8/2023 Problem 2
#Author: nmessa
#fraction.py
#implementation of Fraction class

class Fraction:
    def __init__(self, num, den):
        self.num = int(num)
        if den != 0:
            self.den = int(den)
            self.decimal = num/den
            self.reduce()
        else:
            print ("Invalid fraction")
            self.den = 1
        
    def reduce(self):
        div = self.gcd(self.num, self.den)
        self.num = self.num // div
        self.den = self.den // div

    def gcd(self, a, b):
        while b != 0:
            t = b
            b = a % b
            a = t
        return a

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def add(self, other):
        n = self.num * other.den + other.num * self.den
        d = self.den * other.den
        temp = Fraction(n, d)
        return temp

    def subtract(self, other):
        n = self.num * other.den - other.num * self.den
        d = self.den * other.den
        temp = Fraction(n, d)
        return temp

    def multiply(self, other):
        n = self.num * other.num
        d = self.den * other.den
        temp = Fraction(n, d)
        return temp

    def divide(self, other):
        n = self.num * other.den
        d = self.den * other.num
        temp = Fraction(n, d)
        return temp

#Code to test the Fraction class
f1 = Fraction(1, 2)
f2 = Fraction(3, 4)
print (f1)
print (f2)
f3 = Fraction(6, 8)
print (f3)
f4 = f1.multiply(f2)
f5 = f1.add(f2)
f6 = f1.subtract(f2)
f7 = f1.divide(f2)

print (f1, '*', f2, '=', f4)
print (f1, '+', f2, '=', f5)
print (f1, '-', f2, '=', f6)
print (f1, '/', f2, '=', f7)

        
