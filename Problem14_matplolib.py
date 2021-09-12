###Problem #14 ####
import matplotlib
import numpy as np
pointlist=[-1,5,2,7,3,-1,4,2,6,4]

point_array=np.array(pointlist)
point_matrix=point_array.reshape((5,2))
print(point_matrix)
x=point_matrix[:,0]
print("x=",x)
y=point_matrix[:,1]
print("y=",y)

matplotlib.pyplot.plot(x,y,"go")








