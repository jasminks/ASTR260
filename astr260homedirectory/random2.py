#from pylab import plot
#from pylab import show

N=100
a=21572657
c=96749
m=8089361925
x=1
results=[]
for i in range(N):
  x=(a*x+c)%m
  results.append(x)
  print (x/m*7)
#plot(results,"o")
#show()

#print results
