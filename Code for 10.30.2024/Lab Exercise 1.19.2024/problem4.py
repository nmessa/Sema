##Lab Exercise 1.19.2024 Problem 4
##Author: nmessa

def is_narcissistic(number):
    num = str(number)
    length = len(num)
    total = 0
    for i in range(length):
        total += int(num[i])**length
    if total == number:
        return True
    else:
        return False

print(is_narcissistic(8208))
print(is_narcissistic(22))
print(is_narcissistic(9))
        
##Output
##True
##False
##True
