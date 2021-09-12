###Problem #11 ####
import numpy as np
import random as random

alist=[]
for i in range(0,9,1):
    element=random.randint(2,10)
    alist.append(element)

print (alist)
a=np.array(alist)
print(a.reshape((3,3)))
