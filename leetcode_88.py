from collections import Counter
n=[1,2,3,1]
d=dict(Counter(n))
print(d)
g=[]
for ke,val in d.items():
    if val>1:
        g.append(True)
    else:
        g.append(False)
print(any(g))
