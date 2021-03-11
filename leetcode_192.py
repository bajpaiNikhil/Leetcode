








nums=[17,13,11,2,3,5,7]

d=[]


for i in sorted(nums)[::-1]:
    d=[i]+d[-1:]+d[:-1]
    print(d)
print(d)

