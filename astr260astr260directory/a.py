
import numpy
from numpy import loadtxt
from numpy.fft import rfft

z=loadtxt("piano.txt",float)
x=len(z)
fc=rfft(z)
print x
