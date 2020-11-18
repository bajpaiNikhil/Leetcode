

mat=[[3,3,1,1],[2,2,1,2],[1,1,1,2]]


row=[[i for i in r] for r in mat]
print(row)

col = zip(*mat)
print(col)
for i in col:
    print(i)