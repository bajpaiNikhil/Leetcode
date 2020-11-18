n=2
m=3
indices=[[0,1],[1,1]]

M=[[0 for _ in range(m)] for _ in range(n)]
for r,c in indices:
    for j in range(m):
        M[r][j]^=1
    for i in range(n):
        M[i][c]^=1
print(sum(M[i][j] for i in range(n) for j in range(m)))

