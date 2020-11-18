

from collections import defaultdict

n=[3,3,3,3,3,1,3]
res=[]

d=defaultdict(list)

for i ,gs in enumerate(n):
    d[gs].append(i)

for id,val in d.items():
    i=0
    while(i<len(val)):
        res.append(val[i:i+id])
        i+=id

print(res)
print(d[3])
print(d)