## Lab Exercise 12/19/2023 Problem 4
##Author: nmessa
## 2w + 3x + 4y -5z = -6
## 6w + 7x -8y + 9z = 96
## 10w + 11x + 12y + 13z = 312
## 14w + 15x + 16y + 17z = 416

from pylab import *

M = array([[2, 3, 4, -5], [6, 7, -8, 9], [10, 11, 12, 13], [14, 15, 16, 17]])
V = array([-6, 96, 312, 416])

print (solve(M, V))

## Output
## [  3.   5.   7.  11.]
