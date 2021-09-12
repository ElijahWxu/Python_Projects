## This is problem 12
import numpy as np

a0=input()
a1=input()
a2=input()
a3=input()


numbers=np.array([int(a0),int(a1),int(a2),int(a3)])

print(numbers)
ax=np.sort(numbers)[::-1]
print(ax)

