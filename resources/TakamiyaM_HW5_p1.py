from math import sqrt

accuracy = 3.E-8 
G = 6.674E-11
M = 5.974E24
m=7.348E22
R=3.844E8
omega=2.662E-6
xM = R/(1.+sqrt(M/m))
#def lagrange1(r):
	
r=0.001*R 
delta = 1.0
while abs(delta) > accuracy:
	
	delta = -(G*M/r**2 - G*m/(R-r)**2 - omega**2*(r-sqrt(m/M)*xM))/(2*G*M/r**3+2*G*m/(R-r)**3+omega**2)
        print r,delta
        r -= delta

print r 

#print "Center of mass distance"
#
#rm = R/(1.-M/m)
#print r-rm
