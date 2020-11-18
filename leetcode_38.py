m=[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
d={}
# print(0,m[0].count(1))
# print(1,m[1].count(1))
# print(2,m[2].count(1))
# print(3,m[3].count(1))
# print(4,m[4].count(1))
k=3
for i in range(len(m)):
    d[i]=m[i].count(1)
print(d)

sorted={
    row:value for (row,value) in sorted(d.items(),key=lambda item : item[1])[:k]
}
print (list(sorted.keys()))