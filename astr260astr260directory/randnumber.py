#print 4 random numbers between 0 and 10
from random import randrange
#fix number 
from random import seed
seed(42)
for i in range (4):
   y=randrange(10000)

   print y
