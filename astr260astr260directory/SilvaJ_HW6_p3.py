from math import sin
from numpy import arange,array
from pylab import plot,xlabel,ylabel,show

#defining constants
A=1
B=Y=0.5
Z=2

#defining functions, the Lotka-Volterra functions
def f(r,t):
  x = r[0]
  y = r[1]
  fx = (A*x)-(B*x*y)
  fy = (Y*x*y)-(Z*y)
  return array ([fx,fy],float)

a = 0.0
b = 30.0
N = 10000
h = (b-a)/N


tpoints = arange(a,b,h)
xpoints = []
ypoints = []

r = array ([2.0,2.0], float)
for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[1])
        k1 = h*f(r,t)
        k2 = h*f(r+0.5*k1,t+0.5*h)
        k3 = h*f(r+0.5*k2,t+0.5*h)
        k4 = h*f(r+k1,t+h)
        r += (k1+2*k2+2*k3+k4)/6

plot(tpoints,xpoints,"cyan")
plot(tpoints,ypoints,"green")
xlabel("t")
show()



