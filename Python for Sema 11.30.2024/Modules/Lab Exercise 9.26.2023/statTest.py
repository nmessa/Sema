##Program to test statistics module
##Author: nmessa
##Date: 9.26.2023

import random
from  statistics import *

#create an empty list
numbers = []

#generate list
for _ in range(1000):
    numbers.append(random.randint(1, 10000))

print ('Mean =', calcMean(numbers))
print ('Median =', findMedian(numbers))
print ('Max value =', findLargest(numbers))
print ('Min value =', findSmallest(numbers))
print ('Range =', findRange(numbers))

##Sample Output
##Mean = 4995.499
##Median = 4998.0
##Max value = 9975
##Min value = 4
##Range = 9971

