## Lab Exercise 12/19/2023 Problem 1
## Author: nmessa
## x + y + z = 25000
## 0.06x + 0.07y + 0.08z = 1620
## y - z = 6000

from pylab import *

M = array([[1,1,1], [0.06, 0.07, 0.08], [0,1,-1]])
V = array([25000, 1620, 6000])

print (solve(M, V))

## Output
## [ 15000.   8000.   2000.]
