#
# n=[1,2,3,4]
#
# li=1
# r=10
#
# #
# # l=[]
# #
# # for i in range(len(n)):
# #     suum=0
# #     for j in range(i,len(n)):
# #         suum+=n[j]
# #         print(suum,n[j])
# #         l.append(suum)
# # l.sort()
# # # print(l)
# # #
# # # print(l[li:r])
# # d=sum(l[li:r])
# # m=10**9 + 7
# # print(m)
# # print((sum(l[li-1:r]))%(10^9 + 7))
#
#
#
#
#
# import heapq
# h = [(x, i) for i, x in enumerate(n)]  # min-heap
# heapq.heapify(h)
#
# ans = 0
# for k in range(1, r + 1):  # 1-indexed
#     x, i = heapq.heappop(h)
#     if k >= li: ans += x
#     if i + 1 < len(n):
#         heapq.heappush(h, (x + n[i + 1], i + 1))
# print(ans % 1_000_000_007)

#https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/discuss/730973/Python3-priority-queue



# from collections import  Counter
#
# # n=[5, 9, 2, 9, 7, 2, 5, 3]
# t=int(input())
# for t in range(t):
#     m=int(input())
#     n=list(map(int,input().split()))
#     d=(Counter(n))
#     # print(d)
#     e=list(d.values())
#     # print(e)
#     f=Counter(e)
#     # print(f)
#     l=f.most_common(1)
#     #print(l)
#     z=[]
#     # print(l[0][0])
#     for i ,j in f.items():
#         # print(i,j)
#         if j==l[0][1]:
#             z.append(i)
#     print(min(z))




t=int(input())
for t in range(t):
    m=int(input())
    n=list(map(int,input().split()))[:m]
    z="".join(map(str,n))
    count=0
    maxcount=0
    for i in range(m):
        if n[i]==1:
            count=0
        else:
            count+=1
            maxcount=max(maxcount,count)
            #print(count)
            #print(maxcount)
    #print(maxcount)
    # p=[0]*maxcount
    # p="".join(map(str,p))
    # d=z.count(p)
    # #print(d)
    # if d%2==0:
    #     print("No")
    # else:
    #     print("Yes")
    if maxcount%2==0:
        print("No")
    else:
        # print("Yes")
        p = [0] * maxcount
        p = "".join(map(str, p))
        d = z.count(p)
        # print(d)
        if d >= 2 :
            print("No")
        else:
            print("Yes")

# n=[1 ,0, 0, 0, 1, 0 ,0, 0, 1]
# d="".join(map(str,n))
# print(d)
# r=[0]*3
# r="".join(map(str,r))
# print(d.count(r))

"""
2
9
1 0 0 0 1 0 0 0 1
10
1 0 0 0 1 0 0 0 1
"""
