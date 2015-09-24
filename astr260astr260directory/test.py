def f(x):
        from math import e
	return x**3/(e**x - 1.)  

a=0.
b = input("Enter upper integration limit: ")
h=0.1
N=int((b-a)/h)

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
print "Calculated SB constant using the  Simpson  rule is",s

