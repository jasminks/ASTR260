def f(x):
	return x**4-2*x+1

a=0.
b=2.

# The analytical solution yields: 
sa=4.4

print "Marianne Takamiya - 23 September 2014\n"
print "The numerical integration of Int(x^4-2x+1)dx between x=0 and 2 with"
Nlist=[10,100,1000]
for N in Nlist:
  print N,"slices"
  if N%2!=0:
	N=N+1
  h=(b-a)/N

  s1 = 0.
  s2 = 0.
  st = 0.5*f(a) + 0.5* f(b) 
  for k in range(1,N/2+1):
	s1+=f(a+(2*k-1)*h)
  #        print k, s1

  for k in range(1,N/2):
        s2+=f(a+2*k*h)
  #        print k

  for k in range(1,N):
        st+=f(a+k*h)

  s = h/3.*(f(a)+f(b)+4*s1+2*s2)
  st = st*h

  # Error compared to analytical solution:
  er=abs(sa-s)/sa

  # Print results to screen
  print "using the Simpson rule is",s,"with fractional error",er
  print "using the Trapezoid rule is",st,"\n"

#  print "The fractional error with Simpson's rule compared to the analytical solution",sa,"is",er,"%\n"




