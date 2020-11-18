n=[4,2,1,1,2]
k=1
m=max(n)
l=[]
for i in n:
    if i+1>=m:
        l.append(True)
    else:
        l.append(False)

print(l)