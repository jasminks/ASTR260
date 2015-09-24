from random import random
from numpy import arange
from pylab import plot,show,annotate

NBi213 = 10000
tauBi213 = 46.*60.  # decay life time of Bi 213 in seconds
tauTl209 = 2.2*60.  # decay life time of Tl 209 in seconds
tauPb209 = 3.3*60.  # decay life time of Pb 209 in seconds

NPb209 = 0
NBi209 = 0
NTl209 = 0

decay1=0
decay2 = 0
decay3 = 0

# Branch probabilities
pbranch1 = 0.9791
pbranch2 = 0.0209

# Get the times and ranges:
dt = 1.   
tmax = 20000.

# Initiliaze arrays:
Bi213points = []
Bi209points=[]
Pb209points=[]
Tl209points=[]

#Bi213points.append(NBi213)
#Bi209points.append(NBi209)
#Pb209points.append(NPb209)
#Tl209points.append(NTl209)

# Decay probabilities:
pBi213= 1.-2.**(-dt/tauBi213)
pTl2Pb209 = 1.-2.**(-dt/tauTl209)
pPb2Bi209 = 1.-2.**(-dt/tauPb209)

# Get all time points ready:
tpoints = arange(0.,tmax,dt)

# Check every second:
for t in tpoints:

    # Decay of Pb 209
    # a part of exercise
    for i in range(NPb209):
    	if random() < pPb2Bi209:
       		NBi209 += 1
                NPb209 -= 1
    
    # Decay of Tl 209
    for i in range(NTl209):
    	if random() < pTl2Pb209:
       		NPb209 += 1
                NTl209 -= 1

    # Decay of Bi 213:
    for i in range(NBi213):
        if random()<pBi213:
            NBi213 -= 1
            
            if random()>pbranch1:
       		# Decay of Bi 213 in 97.9% branch
                NPb209 += 1
            else:
                # Decay of Bi 213 in 2.09% branch
            
       		NTl209 += 1

    Bi213points.append(NBi213)
    Bi209points.append(NBi209)
    Pb209points.append(NPb209)
    Tl209points.append(NTl209)

                



plot(tpoints,Bi213points)
plot(tpoints,Bi209points)
plot(tpoints,Pb209points)
plot(tpoints,Tl209points)

annotate('Bi 213', xy=(1000,9000),xytext=(1000,9000),color='b')
annotate('Bi 209', xy=(15000,9000),xytext=(15000,9000),color='g')
annotate('Pb 209', xy=(2000,1000),xytext=(2000,1000),color='r')
annotate('Tl 209', xy=(4500,750),xytext=(4500,750),color='c')
show()
