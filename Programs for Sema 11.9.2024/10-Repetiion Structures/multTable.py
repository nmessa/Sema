#multTable.py
#Author: nmessa
#Date: 11.6.2023

table = int(input("Enter the times table you would like to generate: "))

for i in range(1, 13):
    print(table, "x", i, "=", table*i)

##Sample Output
##8 x 1 = 8
##8 x 2 = 16
##8 x 3 = 24
##8 x 4 = 32
##8 x 5 = 40
##8 x 6 = 48
##8 x 7 = 56
##8 x 8 = 64
##8 x 9 = 72
##8 x 10 = 80
##8 x 11 = 88
##8 x 12 = 96
