
from collections import Counter

arr = [2,2,2,3,3]

d=Counter(arr)
print(d)
l=[]
for i,j in d.items():
    if i==j:
        l.append(j)
print(l)
print(-1 if len(l)==0 else max(l))
