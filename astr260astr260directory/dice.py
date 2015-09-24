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

print x

  #if double ace
  if x==y & x==1: 
    counter+=1
  if x==z & x==1:
    counter+=1
  if x==a & x==1: 
    counter+=1
  if x==b & x==1: 
    counter+=1
  if y==z & y==1: 
    counter+=1
  if y==a & y==1: 
    counter+=1
  if y==b & y==1: 
    counter+=1
  if z==a & z==1:
    counter+=1
  if z==b & z==1:
    counter+=1
  if a==b & a==1:
    counter+=1
print counter 

print float(counter)/N
