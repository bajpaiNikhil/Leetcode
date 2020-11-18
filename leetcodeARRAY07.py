

#
# n=[3,2,3,1,2,4,5,5,6]
# l=len(n)
# k=4
# n.sort()
# print(n)
# print(n[l-k])


import  _heapq
n= [1,2,3]
k=2
maxheap=_heapq._heapify_max(n)
# print(_heapq._heappop_max(n))
# print(_heapq._heappop_max(n))
# print(_heapq._heappop_max(n))
# print(_heapq._heappop_max(n))


for i in range(k):
    _heapq._heappop_max(n)
    if i==k-2:
        print(_heapq._heappop_max(n))
