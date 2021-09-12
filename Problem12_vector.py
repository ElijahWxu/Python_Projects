###Problem #12 ####
import numpy as np
n=10-1
nstart=5
nend=50
dn=(nend-nstart)/n
print (dn)

alist=[]
for i in range(0,n+1,1):
    alist.append(i*dn+5)
    

print (alist)
aVector=np.array(alist)
print(aVector.reshape((10,1)))
asquare=aVector**2          # method 1 for square
#asquare2=aVector*aVector   # Method 2 for square a vector
print (asquare)
