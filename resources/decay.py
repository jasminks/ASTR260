from __future__ import print_function,division

from random import random
from numpy import arange
from pylab import plot,xlabel,ylabel,show

# Constants
NPb = 0               # Number of lead atoms
NTl = 1000            # Number of thallium atoms
tau = 3.053*60        # Half life of thallium in seconds
h = 1.0               # Size of time-step in seconds
p = 1 - 2**(-h/tau)   # Probability of decay in one step
tmax = 1000           # Total time

# Lists of plot points
tlist = arange(0.0,tmax,h)
Tllist = []
Pblist = []

# Main loop
for t in tlist:
    Tllist.append(NTl)
    Pblist.append(NPb)

    # Calculate the number of atoms that decay
    decay = 0
    for i in range(NTl):
        #if random()<p:
	rr=random()
	#print (rr,p)
        if rr<p:       
            decay += 1
    #print (rr,p,decay)
    NTl -= decay
    NPb += decay
    
   # print (NTl, NPb)
# Make the graph
plot(tlist,Tllist)
plot(tlist,Pblist)
xlabel("Time")
ylabel("Number of atoms")
show()
