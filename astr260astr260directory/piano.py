#importing necessary components to plot from modules

from pylab import plot
from pylab import show
import numpy
from numpy import loadtxt
from numpy import linspace


z=loadtxt("piano.txt",float)

#plot????
n=z[:,0]

#this plot will show number of sunspots as a function of time

plot (n)
show()
