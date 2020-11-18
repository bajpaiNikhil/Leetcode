from collections import Counter
n=[4,3,2,7,8,2,3,1]
d=dict(Counter(n))
l=[]
for k,v in d.items():
    if v==2:
        l.append(k)
print(l)
        