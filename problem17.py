print ("Please input three integer numbers")
a1=int(input())
a2=int(input())
a3=int(input())
a_in=[a1,a2,a3]
print (a_in)
a_sort=sorted(a_in)
print (a_sort)

if a_sort==a_in:
    print ("TRUE")
else:
    print("FALSE")