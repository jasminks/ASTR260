import math

N=12
w=math.pi/N
s=0
for k in range (1,N+1):
  xsubi=math.cos((2.*k-1)/(2.*N)*(math.pi))
  s+=(xsubi/(((5./4)-xsubi)**(3./2)))

print s*w
