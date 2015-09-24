#importing necessary components to plot from modules

from pylab import plot
from pylab import show
import numpy
from numpy import loadtxt

#importing sunspot file as an array to plot
z=loadtxt("piano .txt",float)

plot(z)
show()
