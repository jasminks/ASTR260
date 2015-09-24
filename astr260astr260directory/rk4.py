from math import sin
from numpy import arange,array
from pylab import plot,xlabel,ylabel,show

#defining constants
#A is sigma
#B is r
#Z is b

A=10.
B=28.
Z=(8./3)

#defining functions, the Lotka-Volterra functions
def f(r,t):
  x = r[0]
  y = r[1]
  z = r[2]
  fx = A*(y-x)
  fy = B*x-y-x*z
  fz = x*y-Z*z
  return array ([fx,fy, fz],float)

#a is intital time
#b is ending time
a = 0.0
b = 50.0
N = 10000
h = (b-a)/N


tpoints = arange(a,b,h)
xpoints = []
ypoints = []
zpoints = []

#array of inital conditions
r = array ([0.0,1.0,0.0], float)
for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[1])
        zpoints.append(r[2])
        k1 = h*f(r,t)
        k2 = h*f(r+0.5*k1,t+0.5*h)
        k3 = h*f(r+0.5*k2,t+0.5*h)
        k4 = h*f(r+k1,t+h)
        r += (k1+2*k2+2*k3+k4)/6

#plot(tpoints,xpoints,"cyan")
plot(tpoints,ypoints,"cyan")
#plot(tpoints,zpoints,"blue")
xlabel("t")
show()



