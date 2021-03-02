







rowsum=[3,8]
colsum=[4,7]

n=len(rowsum)
m=len(colsum)

ans=[[0]*n for i in range(m)]
ii,j=0,0
while ii<n and j <m:

    x=min(rowsum[ii],colsum[j])
    #print(x)
    ans[ii][j]=x
    print(ans[ii][j])
    rowsum[ii]-=x
    colsum[j]-=x
    if rowsum[ii]==0:
        ii+=1
    if colsum[j]==0:
        j+=1
print(ans)