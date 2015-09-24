from math import tahn,cosh
accuracy= 1*(10**-12)
def arctanh(u):
   x=0.0
   deltax=1.0
   while abs(deltax)>accuracy:
        deltax=(tanh(x)-u)*cosh(x)**2
        x=delta x
   return x
