n=[3,4,5,2]
d=[]
l=[]
for i in n:
    d.append(i-1)
print(d)

d=sorted(d)
print(d[-1]*d[-2])
# for i in range(len(d)):
#     for j in range(i,len(d)):
#         if i!=j:
#             f=d[i]*d[j]
#             if f not in l:
#                 l.append(f)
# print(l)
# print(max(l))