##45.1 Fill list with a function###
import numpy as np
#import math

def h(x):
    return 1/np.sqrt(2*np.pi)*np.exp(-0.5*x**2)

n=41                # number of points along x
x1=-4;x2=4
dx=(x2-x1)/(n-1)   # spacing between two points

xlist=[-4+i*dx for i in range(n)]
hlist=[h(x) for x in xlist]
pairs = [(x,h) for x,h in zip(xlist,hlist)]
print (pairs)