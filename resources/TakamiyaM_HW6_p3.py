from numpy import arange, array
from pylab import plot,xlabel,ylabel,show, legend, ylim

sigma = 10.
rr = 28.
bb = 8./3.

t1=0.
t2=50.

def f(r,t):
    x = r[0]
    y = r[1]
    z = r[2]
    fx = sigma*(y-x)
    fy = rr*x - y - x*z
    fz = x*y - bb*z
    return array([fx,fy,fz],float)

def solve(n):
    h = (t2-t1)/n

    tpoints = arange(t1,t2,h)
    xpoints = []
    ypoints = []
    zpoints = []
    
    # Initial values of x and y:
    xi = 0.
    yi = 1.
    zi = 0.
    
    r = array([xi, yi, zi],float)
    for t in tpoints:
        #print r[0],r[1]
        xpoints.append(r[0])
        ypoints.append(r[1])
        zpoints.append(r[2])
        k1 = h*f(r,t)
        k2 = h*f(r+0.5*k1,t+0.5*h)
        k3 = h*f(r+0.5*k2,t+0.5*h)
        k4 = h*f(r+k3,t+h)
        r += (k1+2*k2+2*k3+k4)/6

    plot(tpoints,ypoints,color='b', label='y')
    xlabel("t")
    ylabel("y(t)")
    show()

    plot(xpoints,zpoints,color='b')
    xlabel("z")
    ylabel("x")
    show()

solve(10000)


