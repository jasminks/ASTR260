#pi=3.14159265
#c=3*(10**8)
#h=(6.636*(10**-34))
#k=1.38*(10**-23)

#k2= (2*pi*h*(1/c)*(1/c)*(k**4)*((1/h)**4))
#"k2" is constant beginning of problem
k2=8.66432176013e-09

def f(x):
        from math import e
	return (x**3)/((e**x) - 1.)

a=0.1
b=100
h=0.1
N=int((b-a)/h)

if N%2!=0:
	N=N+1
s1 = 0.
s2 = 0.
st = 0.5*f(a) + 0.5* f(b) 
for k in range(1,N/2+1):
	s1+=f(a+(2*k-1)*h)


for k in range(1,N/2):
        s2+=f(a+2*k*h)


for k in range(1,N):
        st+=f(a+k*h)

s = h/3.*(f(a)+f(b)+4*s1+2*s2)
st = st*h

y = st*k2
#where this is integral multiplied by constant values 
print "SB constant value using the Trapezoid rule is",y,"\n"

