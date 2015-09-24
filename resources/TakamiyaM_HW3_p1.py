def f(x):
        from math import e
	return x**3/(e**x - 1.)  

a=0.
b = input("Enter upper integration limit: ")
h=0.1
N=int((b-a)/h)

print "Marianne Takamiya - 23 September 2014\n"
print "The numerical integration of Int(t^3 / (e^t - 1) ) dt between t=",a,"and",b,"with"

print N,"slices and widths",h
if N%2!=0:
	N=N+1
s1 = 0.
s2 = 0.

for k in range(1,N/2):
	s1+=f(a+(2*k-1)*h)
        s2+=f(a+2*k*h)

s1+=f(a+(N-1)*h)

# At x=0 the integrant is zero from L'Hopitale, thus f(a) = 0.
#s = h/3.*(f(a)+f(b)+4*s1+2*s2)
s = h/3.*(f(b)+4*s1+2*s2)

## Print results to screen
print "using the  Simpson  rule is",s

from scipy import constants
sB = constants.k**4*s/(constants.pi*constants.c*constants.hbar)**2/(4*constants.hbar)
print "The  accepted  value of the Stefan-Boltzmann constant is",constants.sigma,"m^2 kg s^-2 K-1"
print "The calculated value of the Stefan-Boltzmann constant is %0.6e m^2 kg s^-2 K-1" % sB
