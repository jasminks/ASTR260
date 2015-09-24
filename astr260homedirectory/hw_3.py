from gaussxw import gaussxwab
import math

def f(z):
    return ((z/(1.-z))**(3.)/(math.exp((z/(1.-z)))-1.))/((1.-z)**2.)

N=30
a=0.0
b=1.0
x,w=gaussxwab(N,a,b)
s=0.
for k in range(N):
  s+= w[k]*f(x[k])

print(s)


