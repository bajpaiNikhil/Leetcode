a=[3,1,2,4]
b=[]
c=[]
for i in range(len(a)):
    if a[i]%2==0:
        b.append(a[i])
    else:
        c.append(a[i])
d=b+c
print(d)

