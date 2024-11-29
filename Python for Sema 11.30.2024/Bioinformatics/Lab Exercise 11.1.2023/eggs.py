#Egg Sales
#Author: nmessa
#Date: 10.27.2023

#Get user input
numEggs = int(input("Enter the number of eggs to purchase: "))

#Calculate number of doze and leftovers
dozen = numEggs//12
eggs = numEggs % 12

#Determine cost per dozen
if dozen >= 0 and dozen < 4:
    cost = 3.50
elif dozen >= 4  and dozen < 6:
    cost = 3.00
elif dozen >= 6  and dozen < 11:
    cost = 2.50
else:
    cost = 2.00

#Calculate bill
bill = dozen * cost + eggs * cost/12

#Output result
print("The bill is: $" + str(bill))

##Sample Output
##Enter the number of eggs to purchase: 18
##The bill is: $5.25
