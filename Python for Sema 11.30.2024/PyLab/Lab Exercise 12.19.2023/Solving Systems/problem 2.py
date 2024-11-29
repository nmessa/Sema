## Lab Exercise 12/19/2023 Problem 2
## Author: nmessa
## x + y + z = 100
## 0.30x + 0.40y + 0.80z = 39
## 0.80x + 0.40y + 0.30z = 59

from pylab import *

M = array([[1,1,1], [0.30, 0.40, 0.80], [0.80, 0.40, 0.30]])
V = array([100, 39, 59])

print (solve(M, V))

## Output
## [ 50.  40.  10.]
