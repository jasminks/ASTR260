from pylab import plot, show, xlabel, ylabel,xlim, yscale, ylim

# Part 1a of HW 6 for ASTR 260 Fall 2014
month=[]
n_sunspots=[]
# Reading a file and assigning each column to a different variable
sunspots = open("sunspots.txt", "r")
for aline in sunspots:
    data = aline.split()
    month.append(data[0])
    n_sunspots.append(float(data[1]))
sunspots.close()

plot(month, n_sunspots)
xlabel("Time [months]")
ylabel("Number of Sunspots")
xlim(-50,3200)           
show()

# Part 1b of HW 6 
# Using the mydft.py and myfft codes we worked in class:

# This is part of the Discrete Fourier Transform code mydft.py
from numpy import zeros
from cmath import exp,pi 

def dft(y):
    N = len(y)
    c = zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*exp(-2j*pi*k*n/N) 
    return c

# This is taken from the Fast Fourier Transform code myfft.py
c = dft(n_sunspots)
print len(c)
plot((abs(c)))
yscale('log')
#xlim(-10,10)
show()

plot((abs(c)))
show()

