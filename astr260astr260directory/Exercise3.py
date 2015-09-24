from numpy import dot,empty
from random import random 
 
def f(r):
  # print dot(r,r)
  if dot(r,r) <=1:
      return 1
  else: 
      return 0

N = 1000000
s = 0.0
d = 10  #dimension

for i in range (N):
    r = empty (d, float)
#Generate a random 10 dimension vector r:
#r = [x1, x2, x3, .... x10]
    for k in range (d):
        r[k]=(2.*random())-1 
    s+=float(f(r))

print r
print s
print (s/N*(2.**d))
