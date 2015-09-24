from math import sin
from random import random

def f(x):
    return (sin(1./(x*(2-x))))**2

n = 1999
bigf = 0.
maxx = -1.

for i in range(n):
    x = float(i+1)/1000.
    newbig = max(f(x),bigf)
    if newbig!= bigf:
        bigf = newbig
        maxx = x
print maxx,bigf

n=100
ksum = 0
A = 2.*bigf
print A

for i in range(n):
    x = 2*random()
    y = random()
    if y < f(x):
       ksum += 1

I = A*float(ksum)/n
print I
