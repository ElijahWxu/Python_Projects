###Problem 4.3  ####
import os
cwd = os.getcwd()
print (cwd)

tempfile=["Temperature Data","-----","Fahrenheit degree:67.2"]
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

data=ax[2].split(":")[1]
temp_in_F=float(data)
print ("The temperature is", temp_in_F,"F")

temp_in_C=5/9*(temp_in_F-32)

print ("The temperature is", temp_in_C,"C")

