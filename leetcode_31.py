from collections import Counter

n=[1,2,2,1,1,3]
m=set()
d=Counter(n)
print(d[1])
for i in d.values():
    if i in m:
        print("false")
    else:
        m.add(i)
print(m)
