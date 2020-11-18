s="ibpbhixfiouhdljnjfflpapptrxgcomvnb"

k=33
vowel=["a","e","i","o","u"]
f=list(s)
print(f)
print(len(f))
l=[]

for i in range(len(f)):
    if f[i] in vowel:
        f[i]=1
    else:
        f[i]=0
print(f)

if not len(f)>k:
    print(0)

curr=sum(f[:k])
print(curr)
max_sum=0
for i in range(len(f)-k):
    curr=curr - f[i] + f[i+k]
    print(curr,f[i],f[i+k])
    max_sum=max(curr,max_sum)
    print(max_sum)
print(max_sum)



# for i in range(len(f)-k+1):
#     #print(i)
#     v=0
#     for j in range(k):
#         #print(f[i+j])
#         if f[i+j] in vowel:
#             v+=1
#
#     #print(v)
#     l.append(v)
# print(max(l))

