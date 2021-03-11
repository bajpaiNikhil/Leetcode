










nums = [1,2,3,1]
k = 3
d={}
for i,j in enumerate(nums):
    if j in d and i-d[j]<=k:
        print(True)
    d[j]=i
print(False)


