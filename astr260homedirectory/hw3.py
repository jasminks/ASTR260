import math

def f(x):
    return (math.exp(-x))/(1.0-(math.exp(-x))*(x**3.))
    
a=0.0
#choose b several times until number converges, this represents going towards infinity
b=10.
h=0.01
N=int((b-a)/h)

print "Jasmin Silva's integration of exercise"

s1=0.
s2=0.
st=0.5*f(a)+0.5*f(b)
for k in range(1,N/2+1):
    s1+=f(a+(2*k-1)*h)


for k in range(1,N/2):
        s2+=f(a+2*k*h)
       

for k in range(1,N):
        st+=f(a+k*h)

s = h/3.*(f(a)+f(b)+4*s1+2*s2)
print f(a),f(b)
st = st*h

print "using the  Simpson  rule is",s
print "using the Trapezoid rule is",st,"\n"
