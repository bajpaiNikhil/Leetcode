
from collections import  Counter

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
arr=[]
d=Counter(arr1)
print(d)

for i in arr2:
    print(d[i])
    arr.extend([i]*d[i])
print(arr+[i for i in arr1 if i not in arr2])