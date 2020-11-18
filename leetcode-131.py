
grid=[[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]

row=list(map(max,grid))
col=list(map(max,*grid))
d=sum(map(sum,grid))

print(d)
res=sum(min(i,j) for i in row for j in col)-d
print(res)