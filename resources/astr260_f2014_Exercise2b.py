from math import sin
from random import random

def f(x):
    return (sin(1./(x*(2-x))))**2


a = 0.
b = 2.
N=10000
sum = 0.

for i in range(N):
    x = 2*random()
    sum += f(x)

I = (b-a)/N*sum
print I
