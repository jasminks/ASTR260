from numpy import array
from numpy.linalg import eigh

A=array[[1,2],[2,1],float]

X,V=eigh(A)

print x
print V

#x is eigen values
#V is eigen vectors
