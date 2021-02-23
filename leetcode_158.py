


nums=[2,1,3,4]


n=len(nums)
l=[]
print(sum(nums[i] < nums[i-1] for i in range(len(nums))) <=1)

for i in range(n):
    if nums[i]<nums[i-1]:
        l.append(1)
    else:
        l.append(0)
print(l)
print(sum(l)<=1)