from numpy import loadtxt
from pylab import plot,xlim,show
from mydft import dft 

y = loadtxt("pitch.txt",float)
c = dft(y)
plot(abs(c))
xlim(0,500)
show()

