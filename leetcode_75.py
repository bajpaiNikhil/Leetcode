from collections import Counter
n=[2,2,1,1,1,2,2]
a=len(n)
d=dict(Counter(n))
print(d)
for key,val in d.items():
    if val>a//2:
        print (key)
