from gaussxw import gaussxw
from math import e
import math

def f(x):
    return e**(-(x**2/2.))

N=3.
a=-1.
b=1.

# Calculate the sample points and weights
x,w = gaussxw(N)

# Map sample points and weights to integration limits
xp = 0.5*(b-a)*x + 0.5*(b+a)
wp = 0.5*(b-a)*w

# Perform integration
s=0.
for k in range(N):
    s += wp[k]*f(xp[k])

print s

