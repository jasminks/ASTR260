from numpy import array,empty

A=array([[ 4., -1., -1., -1.],
         [ 1., -3.,  0.,  1.],
         [ 1.,  0., -3.,  1.],
         [ 1.,  1.,  1., -4.]], float)

V0 = array([ 5, 0, -5, 0], float)

N = len(V0)

# Gaussian elimination

for m in range(N):

	# Divide by the diagonal element
	div = A[m,m]
	A[m,:] /= div
	V0[m] /= div

	# Now subtract from the lower rows
	for i in range(m+1, N):

		mult = A[i,m]
		A[i,:] -= mult*A[m,:]
		V0[i]  -= mult*V0[m]

# Backsubstitution
V = empty(N,float)
for m in range(N-1,-1,-1):
	V[m] = V0[m]
	for i in range(m+1,N):
		V[m] -= A[m,i]*V[i]

print V

	
