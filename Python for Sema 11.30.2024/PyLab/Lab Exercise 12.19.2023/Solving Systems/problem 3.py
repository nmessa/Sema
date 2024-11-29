## Lab Exercise 12/19/2023 Problem 3
##Author: nmessa
## x + y + z = 500
## 7.50x + 4.00y + 3.50z = 3025
## x - 2y = 0

from pylab import *

M = array([[1,1,1], [7.50, 4.00, 3.50], [1, -2, 0]])
V = array([500, 3025, 0])

print (solve(M, V))

## Output
## [ 300.  150.   50.]
