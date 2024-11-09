#printVertical.py
#Author: nmessa
#Date: 11.6.2023

#Method 1
name = input("Enter your name: ")
for i in range(len(name)):
    print(name[i])
print()
print()

#Method 2
for letter in name:
    print(letter)
