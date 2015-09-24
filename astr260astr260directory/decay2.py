#from __future__ import print_function,division

from random import random
from numpy import sort
from pylab import plot,xlabel,ylabel,show,xlim,ylim
from math import log

# Constants
NTl = 10            # Number of thallium atoms
tau = 3.053*60        # Half life of thallium in seconds

# Lists of plot points
Tllist = []
Pblist = []
rrlist = []
tlist=[]

# Main loop
for i in range(NTl) :
	t=-tau/log(2.)*log(1.-random())
	rrlist.append(t)
#print rrlist
rrlistsort = sort(rrlist)
#print rrlistsort

z=rrlistsort
#plot (z)
	
# How many decay at time 1s, 2s, 3s, etc?
t = int(rrlistsort[0])+1
print t 

counter = NTl

for i in range(counter):
	if rrlistsort[i] < t:
		NTl -= 1
 	else:
		Tllist.append(NTl)
		Pblist.append(counter - NTl)
		tlist.append(t)
		t = int(rrlistsort[i])+1
		NTl -= 1

for i in range (len(tlist)):
	Pblist[i] = 1000 - Tllist[i]

print i, tlist[i],Tllist[i]

#plot(tlist,Tllist)
#plot(tlist,Pblist)

xlabel("Time")
ylabel("Number of atoms")
show()
