from __future__ import print_function,division

from math import sin
from random import random

#a
def f(x):
    return (sin(1/(x*(2-x))))**2

N = 10000
count = 0
for i in range(N):
    x = 2*random()
    y = random()
    if y<f(x):
        count += 1

I = 2*count/N
print(I)

#this is the code for "hit or miss" monte carlo method where I ~= kA/N
#where k are the number of points below the curve defined by the integrant, N 
# are the total number of random points and A is the area being integrated

