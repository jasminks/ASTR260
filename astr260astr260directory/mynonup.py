from pylab import plot,show
from math import log, e

tau = 3.053*60.
t=0.
pt=[]
tt=[]
while t<1000.:
	pt.append(log(2.)/tau * e**(-t/tau * log(2.)))
	tt.append(t)
	t += 1

plot(tt,pt)
show()
