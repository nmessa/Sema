##doubleThirty.py
##Author: nmessa
##Date: 12.5.2023
##This program will calculate the value of money if doubling each dayfor 30 days

def doubleThirty(amount):
    value = amount
    total = 0
    for i in range(30):
        total += value
        value = 2 * value
    return total

money = float(input("Enter the amount of money: "))
totalPay = doubleThirty(money)
print("The total pay you earn this month is $" + str(totalPay))

##Sample Output
##Enter the amount of money: 0.01
##The total pay you earn this month is $10737418.23
