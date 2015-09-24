from random import random

#set time intervals, and how long your steps will be (in seconds)
tmin=0
tmax=100000
h=1
N=int((tmax-tmin)/h)

#total number of thalliums
NTl=1000

#halflife, tau
T= 3.053*60

#generate random number
r = random()

def p(t):
  1-2.**(-t/T)

#write code so that if p(t) is greared than random number, NTl decays

for i in range (tmax):
  if p(t) > r:
    counter=+-1

