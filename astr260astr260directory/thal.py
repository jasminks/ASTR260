from random import random
from numpy import arange
from pylab import plot,show

#set time intervals, and how long your steps will be (in seconds)
tmin=0.
tmax=1000
h=1
N=int((tmax-tmin)/h)

#total number of thalliums
NTl=10000
#total number of lead 
NPb=0

#halflife, tau
T= 3.053*60

# Lists of plot points
tlist = arange(0.0,tmax,h)
Tllist = []
Pblist = []

def p(t):
  return 1-2.**(-t/T)

for t in tlist:
   Tlist.append(NTl)
   Pblist.append(NPb)

#write code so that if p(t) is greared than random number, NTl decays

counter=10000
for t in range (tmax):
  if p(t) > random():
    counter+=-1

    #print counter
    NTl -= counter
    NPb += counter
#Plot time
plot(tlist, Tllist)
plot(tlist, Pnlist)
show()
