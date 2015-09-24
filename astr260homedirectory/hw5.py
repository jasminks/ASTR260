accuracy=10**4

G=6.674*(10**-11)
M=5.974*(10**24)
m=7.348*(10**22)
R=3.844*(10**8)
w=2.662*(10**-6)
r=10**8

def f(r): 
  return ((G*M/r**2)-(G*m/((R-r)**2)))-((w**2)*r)
def g(r):
  return ((2*G*m)/((r-R)**3))-((2*G*M)/(r**3)-(w**2))

while abs (f(r)/g(r))> accuracy:
   r1=r-f(r)/g(r)
   r=r1

print r1
