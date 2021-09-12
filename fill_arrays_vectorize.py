###  5.2 Fill list with a function###
import numpy as np
#import math

def h(x):
    return 1/np.sqrt(2*np.pi)*np.exp(-0.5*x**2)

n=41                # number of points along x
x1=-4;x2=4
dx=(x2-x1)/(n-1)   # spacing between two points

xlist=np.linspace(-4,4,41)

print(xlist)

ylist=h(xlist[:])
print(ylist)

pairs = [(x,h) for x,h in zip(xlist,ylist)]
print (pairs)


