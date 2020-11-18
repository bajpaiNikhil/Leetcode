nums = [0,0,0]
k = 1
l=[]
indices = [i for i, x in enumerate(nums) if x == 1]
print(indices)
if len(indices)>1:
    for i in range(len(indices)-1):
        ke=abs(indices[i]-indices[i+1])
        l.append(ke)
        #print(ke)
    print(l)
    if min(l)<=k:
        print(False)
    else:
        print(True)
else:
    print(True)
