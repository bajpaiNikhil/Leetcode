





# for i in range(nlength):
#     for j in range(i,nlength):
#         if n[i]>n[j]:
#             n[i],n[j]=n[j],n[i]
# print(n)
#
# def pivot(n,low,high):
#     i=low-1
#     pi=n[high]
#
#     for j in range(low,high):
#         if n[j] <= pi:
#             i+=1
#             n[i],n[j]=n[j],n[i]
#     n[i+1],n[high]=n[high],n[i+1]
#     return i+1
#
# def QuickSort(n,low,high):
#     if len(n)==1:
#         return n
#     if low<high:
#         pi = pivot(n,low,high)
#         QuickSort(n,low,pi-1)
#         QuickSort(n,pi+1,high)
#     return n
# n=[1,2,7,6,4,5,3]
# low = 0
# high = len(n)-1
# print(QuickSort(n,low,high))




def binarySearch(n,low,high,k):

    while low<=high:
        mid=(low+high)//2

        if n[mid]>k:
            high = mid-1
        elif n[mid]<k:
            low=mid+1
        else:
            return mid
    return -1


n=[1,2,7,6,4,5,3]
n.sort()
print(n)
low=0
high=len(n)-1
k=5
print(binarySearch(n,low,high,k))




list_int = ['1', '12', '15', '21', '131']
list1=map(int,list_int)
print(list(list1))










