



n = [1,2,2,4]
#n=[3,2,2]
#n=[1,2,2]
#n=[1,1]
#n=[3,2,3,4,6,5]
n.sort()
print(n)
nlen=len(n)
l=[i for i in range(1,nlen+1)]
print(l)
#print(l)

res=[]

for i in range(nlen-1):
    if n[i]==n[i+1]:
        res.append(n[i])
print(res)
for j in l:
    if j not in n:
        res.append(j)

print(res)
# for i in range(1,nlen-1):
#     print(i)
#     if n[i]==n[i+1]:
#         #print("1")
#         if n[i]+1 in n and n[i]-1 not in n:
#             #print(n[i+1],n[i])
#             l.append(n[i])#+[l[0]+1]
#             print([l[0]]+[l[0]-1])
#         elif n[i]-1 in n and n[i]+1 not in n:
#             l.append(n[i])#+[l[0]-1]
#             print([l[0]]+[l[0]+1])