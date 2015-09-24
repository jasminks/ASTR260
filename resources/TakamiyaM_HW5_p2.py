from math import exp,log,e
vp=5.
r1=1000.
r2=4000.
r3=3000.
r4=2000.
i0=3.E-9
vt=0.05

r12 = 1./(1./r1+1./r2)
r34 = 1./(1./r3 + 1./r4)

v1 = 1.
v2 = 1.

dv = v1-v2
for k in range(10):
         dv=v1-v2
         v1log= (1.+vp/r1/i0  - v1/i0/r12)           
         v2log= (1.-vp/r3/i0  + v2/i0/r34)           
	 if v1log>0:
         	v1=v2+vt*log(1.+vp/r1/i0  - v1/i0/r12)           
	 else:
                v1=r12*(vp/r1+i0-i0*e**(dv/vt))
		
	 if v2log>0:
	         v2=v1-vt*log(1.-vp/r3/i0  + v2/i0/r34)           
	 else:
	         v2=r34*(vp/r3-i0+i0*e**(dv/vt))
		
	 print v1,v2, v2-v1
	

print 'V1=',v1	
print 'V2=',v2	
print 'Voltage difference across diode is = ',v1-v2
