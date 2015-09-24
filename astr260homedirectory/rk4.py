from __future__ import print_function,division

from math import sin
from numpy import arange
from pylab import plot,xlabel,ylabel,show

a = 0.0
b = 10.0

def f(x,t):
    return -x**3 + sin(t)

def solve(n):
    h = (b-a)/n

    tpoints = arange(a,b,h)
    xpoints = []

    x = 0.0
    for t in tpoints:
        xpoints.append(x)
        k1 = h*f(x,t)
        k2 = h*f(x+0.5*k1,t+0.5*h)
        k3 = h*f(x+0.5*k2,t+0.5*h)
        k4 = h*f(x+k1,t+h)
        x += (k1+2*k2+2*k3+k4)/6

    plot(tpoints,xpoints,"k-")

solve(20)


xlabel("t")
ylabel("x(t)")
show()
