# This program will demonstrate type conversion.  The input function will result
# in the input of a string type.  If we need to do any math to the input data,
# we will need to convert it to a number type.

number = input("Enter a number: ")
print(type(number))

number = int(number)
print(type(number))

number = float(number)
print(type(number))

##Sample output
##Enter a number: 35
##<class 'str'>
##<class 'int'>
##<class 'float'>

##Enter a number: seven
##<class 'str'>
##Traceback (most recent call last):
##  File "F:/Coding Club USB -2024-2025/Code/October 30, 2024/typeConvert.py", line 8, in <module>
##    number = int(number)
##ValueError: invalid literal for int() with base 10: 'seven'

##Enter a number: 3.1415928
##<class 'str'>
##Traceback (most recent call last):
##  File "F:/Coding Club USB -2024-2025/Code/October 30, 2024/typeConvert.py", line 8, in <module>
##    number = int(number)
##ValueError: invalid literal for int() with base 10: '3.1415928'

##Enter a number: 1,000,000
##<class 'str'>
##Traceback (most recent call last):
##  File "F:/Coding Club USB -2024-2025/Code/October 30, 2024/typeConvert.py", line 8, in <module>
##    number = int(number)
##ValueError: invalid literal for int() with base 10: '1,000,000'

##Enter a number: $1.45
##<class 'str'>
##Traceback (most recent call last):
##  File "F:/Coding Club USB -2024-2025/Code/October 30, 2024/typeConvert.py", line 8, in <module>
##    number = int(number)
##ValueError: invalid literal for int() with base 10: '$1.45'



