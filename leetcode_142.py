



a = [1,3,4,8]
q = [[0,1],[1,2],[0,3],[3,3]]
l=[]
for i in range(len(a)-1):
    a[i+1]^=a[i]
print(a)
for i,j in q:
    if i:
        l.append(a[j]^a[i-1])
    else:
        l.append(a[j])
print(l)