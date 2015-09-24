from gaussxw import gaussxwab
from math import e
import math


def f(x):
    return e**(-1*(x**2./2))

N=5
a=-1.
b=1.

x,w = gaussxwab(N,a,b)

s = 0.0
for k in range(N):
  s += w[k]*f(x[k])

print s 

