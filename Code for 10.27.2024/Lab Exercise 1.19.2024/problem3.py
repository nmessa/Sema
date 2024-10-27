##Lab Exercise 1.19.2024 Problem 3
##Author: nmessa

def sort_descending(number):
    numbers = []
    reverse = ""
    number = str(number)
    for num in number:
        numbers.append(int(num))
    numbers.sort(reverse=True)
    for n in numbers:
        reverse += str(n)
    return int(reverse)

print(sort_descending(123))
print(sort_descending(1254859723))
print(sort_descending(73065))

##Output
##321
##9875543221
##76530
