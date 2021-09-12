###Problem #13 ####
import os
cwd = os.getcwd()
print (cwd)

scorelist=[83,93,72,65,80]
#print (scorelist)
with open("score.txt", "w") as f:       # open a file to save the score
     f.write('\n'.join(str(score) for score in scorelist))
f.close()

#open and read the file          
f = open("score.txt", "r")        # open the saved file to read out the scores line by line
ax=f.readlines()
line_count=len(ax)
print(line_count)
print(ax)
f.close()
score_read=[]

for i in range(1,line_count,1):   
    score_read.append(int(ax[i]))

print ("score_read=",score_read)

score_sum=sum(score_read)           # sum of scores
average=score_sum/line_count        # calculate the average score
print ("average score is", average)






