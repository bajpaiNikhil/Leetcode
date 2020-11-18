
#M=[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

"""def counter(M,n,m):

    count=0
    for i in range(n):
        for j in range(m):
            if M[i][j]<0:
                count=count+1
                #print(count)
            else:
                continue
    return count

M = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
n=len(M)
m=len(M[0])
#print(n,m)

print(counter(M,n,m))"""



# def counter(M , start, end,m):
#
#     if start==end:
#         return start
#
#     mid=start+(end-start)//2
#
#     if(M[mid]<0):
#         if(mid+1<m and M[mid+1]>=0):
#             return mid
#
#         return counter(M,mid+1,end,m)
#
#     else:
#         return counter(M,start,mid-1,m)
#
# def countNegative(M1,n,m):
#     count=0
#     nextEnd=m-1
#     for i in range(n):
#         if M1[i][0]>0:
#             continue
#         nextEnd=counter(M1[i],0,nextEnd,4)
#         count+=nextEnd+1
#     return count
#
# M1=[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# n=len(M1)
# m=len(M1[0])
# print(countNegative(M1,n,m))
#




