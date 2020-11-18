from collections import Counter

a=[2,3,1,3,2,4,6,7,9,2,19]
#1 2 2 2 3 4 6 7 9 19
b=[2,1,4,3,9,6]
c=[]
A=dict(Counter(a))
print(A)
for i in b:
    c.extend([i]*(A[i]))
print(c)
c.extend(sorted(x for x in a if x not in b))
print(c)

print(A[2]*[1])



