#Demonstration of range function

print(list(range(10)))

print(list(range(1,10)))

print(list(range(1,10, 2)))

print(list(range(10, 0, -1)))


for i in range(10):
    print(i, end = " ")
print()

for i in range(1, 10):
    print(i, end = " ")
print()

for i in range(1, 10, 2):
    print(i, end = " ")
print()

for i in range(10, 0, -1):
    print(i, end = " ")
print()

for i in range(10, 0, -1):
    print(i)
print("Blast Off!!!")

##Output
##[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
##[1, 2, 3, 4, 5, 6, 7, 8, 9]
##[1, 3, 5, 7, 9]
##[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
##0 1 2 3 4 5 6 7 8 9 
##1 2 3 4 5 6 7 8 9 
##1 3 5 7 9 
##10 9 8 7 6 5 4 3 2 1 
##10
##9
##8
##7
##6
##5
##4
##3
##2
##1
##Blast Off!!!
