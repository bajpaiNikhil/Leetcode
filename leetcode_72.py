n=[2,1,0,3,12]
l=len(n)
count=0
for i in range(l):
    if n[i]!=0:
        n[count]=n[i]
        count+=1
while(count<l):
    n[count]=0
    count+=1
print(n)

