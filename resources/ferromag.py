from math import tanh,cosh
from numpy import linspace
from pylab import plot,show,ylim,xlabel,ylabel

# Constants
Tmax = 2.0
points = 1000
accuracy = 1e-6

# Set up lists for plotting
c = []
temp = linspace(0.01,Tmax,points)

# Temperature loop
for T in temp:
    m = 1.0
    error = 1.0

    # Loop until error is within bounds
    while error>accuracy:
        m,mp = tanh(m/T),m
        error = abs((m-mp)/(1-T*cosh(m/T)**2))
    c.append(m)

# Make the graph
plot(temp,c)
ylim(0.0,1.1)
xlabel("Temperature")
ylabel("Magnetization")
show()
