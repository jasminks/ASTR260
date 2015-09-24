from __future__ import print_function,division

from math import sin
from random import random
from math import e 


def f(x):
    return (x**3)/(e**x - 1.)

N = 10000
count = 0
for i in range(N):
    x = 100*random()
    y = 2*random()
    if y<f(x):
        count += 1

I = 200*count/N

pi=3.14159265
c=3*(10**8)
h=(6.636*(10**-34))
k=1.38*(10**-23)

k2= 2*pi*h*(1/c)*(1/c)*(k**4)*((1/h)**4)
print(I*k2)

#this is the code for "hit or miss" monte carlo method where I ~= kA/N
#where k are the number of points below the curve defined by the integrant, N 
# are the total number of random points and A is the area being integrated

#now, using the mean value method where I~= b-a/N * sum ( f(xi))
#b = 2
#a = 0
