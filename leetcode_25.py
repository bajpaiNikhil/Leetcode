a=[5,1,5,2,5,3,5,4]
# n=len(a)
# mp=[0]*100
# for i in range(n):
#     mp[a[i]]+=1
# for i in range(0,n):
#     if mp[a[i]]>1:
#         print(a[i])
#         mp[a[i]]=0
b=set(a)
c=sum(a)-sum(b)
print(c)
d=len(a)-len(b)
print(d)
print(c//d)