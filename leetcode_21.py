a=[[3,7,8],[9,11,13],[15,16,17]]
n=len(a)
m=len(a[0])
print(n,m)
L1=[]
l2=[]
for i in range(n):
    mim=a[i][0]
    for j in range(1,m,1):
        if  (a[i][j]<mim):
            mim=a[i][j]
    L1.append(mim)
print(L1)

#print(mim)

for i in range(m):
    max=a[0][i]
    for j in range(n):
        if (a[j][i]>max):
            max=a[j][i]
    l2.append(max)
        #print(max)
print(l2)
c=[i for i in L1 if i in l2]
print(c)


matrix=[[3,7,8],[9,11,13],[15,16,17]]
n = len(matrix)
m = len(matrix[0])
l1 = []
l2 = []
for i in range(n):
    mim = matrix[i][0]
    for j in range(1, m, 1):
        if (matrix[i][j] < mim):
            mim = matrix[i][j]
    l1.append(mim)
for i in range(m):
    maax = matrix[0][i]
    for j in range(n):
        if (matrix[j][i] > maax):
            maax = matrix[j][i]
    l2.append(maax)
c = [value for value in l1 if value in l2]
print(c)
