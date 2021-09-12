###Problem 4.4  ####
import os
cwd = os.getcwd()
print (cwd)

tempfile=["Temperature Data","-----","Fahrenheit degree:67.2","Fahrenheit degree:50.2","Fahrenheit degree:39.2"]
print (tempfile)
with open("temp.txt", "w") as f:       # open a file to save the score
     f.write('\n'.join(str(temp) for temp in tempfile))
f.close()



#open and read the file          
f = open("temp.txt", "r")        # open the saved file to read out the scores line by line
ax=f.readlines()
line_count=len(ax)
print(line_count)
print(ax[2])
f.close()

temp_in_F=[]
temp_in_C=[]
for i in range(2,line_count):
    data=ax[i].split(":")[1]
    temp_in_F.append(float(data))
    temp_in_C.append(5/9*(float(data)-32))
    
print ("The temperature list in F is", temp_in_F)

print ("The temperature list in C is", temp_in_C)

