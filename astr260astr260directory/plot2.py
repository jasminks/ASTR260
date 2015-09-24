import pylab
import numpy
import math 

x = numpy.linspace(-15,15,100) # 100 linearly spaced numbers
y = float((x**3)/((numpy.exp(x)-1)))
z = y[:,0] 

# compose plot
pylab.plot(x,z)
pylab.plot(x,z,'co') # same function with cyan dots
#pylab.plot(x,2*y,x,3*y) # 2*sin(x)/x and 3*sin(x)/x
pylab.show() # show the plot
