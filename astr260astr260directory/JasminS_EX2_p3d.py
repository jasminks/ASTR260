
from random import randrange
counter=0

money=10000000
N=money/5

for i in range (N):
  x=randrange(1,14)
  y=randrange(1,14)
  z=randrange(1,14)
  a=randrange(1,14)
  b=randrange(1,14)

  if x==y==1: 
    counter+=1
  if x==z==1:
    counter+=1
  if x==a==1: 
    counter+=1
  if x==b==1: 
    counter+=1
  if y==z==1: 
    counter+=1
  if y==a==1: 
    counter+=1
  if y==b==1: 
    counter+=1
  if z==a==1:
    counter+=1
  if z==b==1:
    counter+=1
  if a==b==1:
    counter+=1
  else:
     counter+=0

print counter

#divided by 10 because 10 terms added
#printed answer justifies mathermatical analysis of probability
print (float(counter)/N)/10

