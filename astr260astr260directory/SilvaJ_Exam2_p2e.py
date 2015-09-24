#importing necessary components to plot from modules

from pylab import plot
from pylab import show
import numpy
from numpy import loadtxt
from numpy.fft import rfft

#importing piano.txt  as an array 
z=loadtxt("piano2.txt",float)
#fft array
fc=rfft(z)
#plotting first 10000 fourier coeff
a=fc[:10000]
#plotting coefficients 
plot(a)
show()
