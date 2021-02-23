
#from itertools import accumulate
a=[-4,-3,-2,-1,4,3,2]

current=0
max_current=0

for i in range(len(a)):
    current+=a[i]
    max_current=max(max_current,current)
print(max_current)