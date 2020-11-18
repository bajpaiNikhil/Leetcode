

n=[5,0,3,8,6]

currentmax=n[0]
permax=n[0]
index=1

for i in range(len(n)-1):
    if n[i] < permax:
        index=i+1
        permax=currentmax
    else:
        currentmax=max(currentmax,n[i])
print(index)