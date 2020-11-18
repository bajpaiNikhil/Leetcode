n=[1,2,7,15]
t=9

# for i in range(len(n)):
#     for j in range(i,len(n)):
#         if i!=j :
#             k=n[i]+n[j]
#             if k == t:
#                 print([i+1,j+1])
l,r=0,len(n)-1
#print(l,r)
while(l<r):
    if n[l]+n[r] == t:
        print(l+1,r+1)
    if n[l]+n[r] > t :
        r-=1
    else:
        l+=1