




from math import sqrt
n=[[1,2],[3,4],[1,-1]]
k=2

n.sort(key=lambda x:sqrt(x[0]**2+x[1]**2))
print(n[:k])


# print(n)
# l=[]
# k=2
# d=0
# for i in n:
#     sqroot=sqrt((i[0]**2) +(i[1]**2))
#     l.append(sqroot)
# print(l)
# o=[]
# for a,b in zip(l,n):
#     d+=1
#     if d<=k:
#         o.append(b)
# print(o)