

from collections import  Counter
n=[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

d={}

for i ,j in n:
    if i not in d:
        d[i]=[[i,j]]
    else:
        d[i].append([i,j])
print(d)
#
# print(sorted(d.keys(),reverse=True))
#print(sorted(d[5]))
re=[]
for h in sorted(d.keys(),reverse=True):
    group=sorted(d[h])
    for h, k in group:
        re.insert(k, [h, k])
print(re)