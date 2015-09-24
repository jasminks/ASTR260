from math import tanh,cosh
accuracy= 1e-12
def arctanh(u):
   x=0.6
   deltax=1.0
   while abs(deltax)>accuracy:
        deltax=(tanh(x)-u)*((cosh(x))**2)
        x-=deltax
   return x
