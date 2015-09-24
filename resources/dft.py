from __future__ import print_function,division

from numpy import empty,loadtxt
from pylab import plot,xlim,show
from cmath import rect,pi

def dft(y):
    N = len(y)
    c = empty(N//2,complex)

    for k in range(N//2):
        s = 0.0
        for n in range(N):
            s += rect(y[n],-2*pi*k*n/N)
        c[k] = s/N

    return c


y = loadtxt("pitch.dat",float)
plot(abs(dft(y)))
xlim(0,500)
show()
