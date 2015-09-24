#Simpson's rule in terms of exercise 5.3, change equation, bounds and N as necessary for problem

import math
def f(x):
  return math.exp(-x**2.)
N=30
A=0.0
B=3.0
C=0.5*(A+B)
h=(B-A)/N
s= ((B-A)/6)*(f(A)+4*f(C)+f(B))
for k in range (1,N):

  s+=f(A+k*h)

print (h*s)
