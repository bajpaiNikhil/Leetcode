# import numpy as np
# mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
#
# a=np.array(mat)
# print(a)
#
# diag=np.diag(a)
# print(diag)
#
# idx=np.argsort(diag)
#
# print(idx)
#
# B=a[idx,:][:,idx]
# print(B)

x,y=3,4
count=0
while (x>0 or y>0):
    count+=(x%2)^(y%2)
    x>>=1
    y>>=1
print(count)