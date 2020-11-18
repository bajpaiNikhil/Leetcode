# import numpy as np
# A=[[1,1,0],[1,0,1],[0,0,0]]
# arr=np.array(A)
# #print(arr)
# b=arr[:,::-1]
# #print(b)
# d={1:0,0:1}
# n=len(b)
# m=len(b[0])
# for i in range(n):
#     for j in range(m):
#         if b[i][j]==0:
#             b[i][j]=1
#         else:
#             b[i][j]=0
# print(b)

#
# indexer = np.array([d.get(i, -1) for i in range(b.min(), b.max() + 1)])
# c=indexer[(b - b.min())]
# print(c)

A=[[1,1,0],[1,0,1],[0,0,0]]
# if a==[[]] or None:
#     print("[[]]")
# for i in range(len(a)):
#     temp=a[i]
#     a[i]=temp[::-1]
#     for j in range(len(a[i])):
#         if a[i][j]==0:
#             a[i][j]=1
#         else:
#             a[i][j]=0
# print(a)

if A == [[]] or None:
    print([[]])
for i in range(len(A)):
    temp = A[i]
    A[i] = temp[::-1]
    for j in range(len(A[i])):
        if A[i][j] == 1:
            A[i][j] = 0
        else:
            A[i][j] =1
print(A)
