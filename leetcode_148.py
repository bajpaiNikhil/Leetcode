

from collections import Counter
n=[1,2,1,3,2,5]

d=Counter(n)
print(d)
l=[]
for i , j in d.items():
    if j==1:
        l.append(i)
print(l)