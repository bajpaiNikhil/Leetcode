import math
n=[4,3,2,7,8,2,3,1]
#=[-3,-2,-1,-6,-7,-1,-3,0]
#=[
for i in range(len(n)):
    j=abs(n[i])-1
    n[j]=abs(n[j])*-1
    #print(n[i])
res=[]
for i in range(len(n)):
    if n[i]>0:
        res.append(i+1)
print(res)

