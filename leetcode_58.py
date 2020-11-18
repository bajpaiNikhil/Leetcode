from collections import Counter

l=[1,1,1,1000]

a=dict(Counter(l))

print(a)
print(len(a))
c=0
if len(l)//2>len(a):
    print(a)
else:
    print(len(l)//2)