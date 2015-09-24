from math import exp
import math 


a=1
b=2


def f(x,y):
  return a*y+x**2*y 
  
def g(x,y):
  return  b/(x**2+a)

for k in range (100):
  x=f(x,y)
  y=g(x,y)
 
print v1,v2
