#importing necessary components to plot from modules

from pylab import plot,show,xlim,ylim
from numpy import loadtxt
from mydft import dft

#importing sunspot file as an array to plot
z=loadtxt("sunspots.txt",float)

#z is now an array

#t is time in months
t=z[:,0]

#n is number of sunspots occuring within that period
n=z[:,1]

for n in npoints:
    xpoints.append()

#taking the dft of the sunspots
c = dft(n)

#plotting fourier coefficients
plot (abs(c)**2)
xlim(0,3142/2)
ylim(0,3*10**9)
show()
