##doubleMoney.py
##Author: nmessa
##Date: 12.5.2023
##This program will calculate how long it takes to double your money
##Interest is paid yearly and the interest rate is an annual rate

def doubleMoney(principle, interestRate):
    years = 0
    value = principle
    while value < 2*principle:
        value = value + value*interestRate/100  #divide by 100 to convert percent to decimal
        years += 1
    return years

amount = float(input("Enter the amount of your deposit: "))
rate = float(input("Enter your interest rate (%): "))

numYears = doubleMoney(amount, rate)
print("It took", numYears, "years to double your money at an interest rate of", rate)

##Sample Output
##Enter the amount of your deposit: 1000
##Enter your interest rate (%): 5
##It took 15 years to double your money at an interest rate of 5.0
