from numpy import linspace
from pylab import plot,show
from atanh import arctanh

upoints=linspace(-0.99,0.99,100)
xpoints=[]
for u in upoints:
    xpoints.append(arctanh(u))
plot(upoints,xpoints)
show()
