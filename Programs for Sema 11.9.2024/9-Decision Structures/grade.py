#grade.py
#Author: nmessa
#Date: 11.14.2023

score = int(input("Enter your test score: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
