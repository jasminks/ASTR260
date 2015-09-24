from gaussxw import gaussxw

def f(x):
    return x**4 - 2*x + 1

N=3
a=0.
b=2.0

# Calculate the sample points and weights
xp = gaussxw(N)

# Map sample points and weights to integration limits
xp = 0.5*(b-a)*x + 0.5*(b+a)
wp = 0.5*(b-a)*w

# Perform integration
s=0.
for k in range(N):
    s += wp[k]*f(xp[k])

print s

