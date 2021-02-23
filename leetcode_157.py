

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

n=(len(mat))
ans=0
mid=n//2

for i in range(n):
    ans+=mat[i][i]
    ans+=mat[n-1-i][i]

if n%2==1:
    ans-=mat[mid][mid]
print(ans)