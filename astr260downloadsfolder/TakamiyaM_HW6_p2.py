from math import sin
from numpy import arange, array
from pylab import plot,xlabel,ylabel,show, legend, ylim

a = 1.
b = 0.5
c = 0.5
d = 2.

t1=0.
t2=30.

def f(r,t):
    x = r[0]
    y = r[1]
    fx = a*x-b*x*y
    fy = c*x*y-d*y
    return array([fx,fy],float)

def solve(n):
    h = (t2-t1)/n

    tpoints = arange(t1,t2,h)
    xpoints = []
    ypoints = []

    # Initial values of x and y:
    xi = 2.
    yi = 2.

    r = array([xi, yi],float)
    for t in tpoints:
        #print r[0],r[1]
        xpoints.append(r[0])
        ypoints.append(r[1])
        k1 = h*f(r,t)
        k2 = h*f(r+0.5*k1,t+0.5*h)
        k3 = h*f(r+0.5*k2,t+0.5*h)
        k4 = h*f(r+k3,t+h)
        r += (k1+2*k2+2*k3+k4)/6

    plot(tpoints,xpoints,color='r', label='Rabbits')
    plot(tpoints,ypoints,color='b', label='Foxes')



solve(1000)
ylim(0,10)
legend( loc='upper left', numpoints = 1 )
xlabel("t")
ylabel("Number of Rabbits and Foxes")
show()
