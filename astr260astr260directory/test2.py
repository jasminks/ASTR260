def f(x):
        from math import e
	return x**3/(e**x - 1.) 

a=0.1
b=3.
h=0.1
N=int((b-a)/h)

print "Marianne Takamiya - 23 September 2014\n"
print "The numerical integration of Int(e^(-t^2)dt between t=",a,"and",b,"with"

print N,"slices and widths",h
if N%2!=0:
	N=N+1
s1 = 0.
s2 = 0.
st = 0.5*f(a) + 0.5* f(b) 
for k in range(1,N/2+1):
	s1+=f(a+(2*k-1)*h)

for k in range(1,N/2):
        s2+=f(a+2*k*h)
        print k, s2

for k in range(1,N):
        st+=f(a+k*h)

s = h/3.*(f(b)+4*s1+2*s2)
print f(a),f(b)
st = st*h

# Print results to screen
print "using the  Simpson  rule is",s
print "using the Trapezoid rule is",st,"\n"

