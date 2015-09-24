#rolling dice
#what is the probability of both dice being 6?

from random import randrange
counter=0

money=10000
N=money/5
for i in range (N):
  #"generate one random number"
  x=randrange(1,14)
  #"generate another random number"
  y=randrange(1,14)
  #"generate another random number"
  z=randrange(1,14)
  a=randrange(1,14)
  b=randrange(1,14)

print x,y,z,a,b
  

