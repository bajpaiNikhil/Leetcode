



m  =[[0,0,0],[0,1,0],[0,1,0],[1,1,1],[1,1,0]]
lenr=3
lenc=4
d=[[0 for i in range(lenr+1)] for j in range(lenc+1)]
print(d)
for ii in range(1,len(m)):
    for jj in range(1,len(m[0])):
        print(ii,jj,ii and jj)
#         if m[ii][jj] and ii and jj:
#             m[ii][jj]+=min(m[ii-1][jj-1],m[ii][jj-1],m[ii-1][jj])
# print(m)
# print(sum(map(sum,m)))