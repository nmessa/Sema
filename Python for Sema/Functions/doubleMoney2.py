##doubleMoney2.py
##Author: nmessa
##Date: 12.5.2023
##This program will calculate how long it takes to double your money
##Interest is paid yearly and the interest rate is an annual rate
##This program calculate years for a variety of interest rates

def doubleMoney(principle, interestRate):
    years = 0
    value = principle
    while value < 2*principle:
        value = value + value*interestRate/100  #divide by 100 to convert percent to decimal
        years += 1
    return years

amount = 1000

for rate in range(1, 11):
    numYears = doubleMoney(amount, rate)
    print("It took", numYears, "years to double your money at an interest rate of", rate)

##Sample Output
##It took 70 years to double your money at an interest rate of 1
##It took 36 years to double your money at an interest rate of 2
##It took 24 years to double your money at an interest rate of 3
##It took 18 years to double your money at an interest rate of 4
##It took 15 years to double your money at an interest rate of 5
##It took 12 years to double your money at an interest rate of 6
##It took 11 years to double your money at an interest rate of 7
##It took 10 years to double your money at an interest rate of 8
##It took 9 years to double your money at an interest rate of 9
##It took 8 years to double your money at an interest rate of 10
