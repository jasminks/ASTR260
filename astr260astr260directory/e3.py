#importing necessary components to plot from modules

from pylab import plot
from pylab import show
import numpy
from numpy import loadtxt
from numpy.fft import rfft

#importing piano.txt  as an array to plot
z=loadtxt("piano2.txt",float)
fc=rfft(z)
a=fc[:10000]
plot(a)
show()
