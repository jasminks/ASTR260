#importing necessary components to plot from modules

from pylab import plot
from pylab import show
import numpy
from numpy import loadtxt

#importing sunspot file as an array to plot
z=loadtxt("sunspots.txt",float)

#z is now an array

#t is time in months
t=z[:,0]

#n is number of sunspots occuring within that period
n=z[:,1]

#this plot will show number of sunspots as a function of time
#the x axis represents times, in months
#the y axis represents number of sunspots 

plot (t,n)
show()
