import math
def f(x):
  return math.exp(-x**2.)
N=30
A=0.0
B=3.0
h=(B-A)/N
s= 0.5*f(A)+0.5*f(B)
for k in range (1,N):

  s+=f(A+k*h)

print (h*s)
