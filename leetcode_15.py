# arr=[17,18,5,4,6,1]
# b=max(arr)
a=[17,18,5,4,6,1]
print(len(a))
def greater(arr):
    size=len(arr)
    next_greater=arr[size-1]
    arr[size-1]=-1
    for i in range(size-2,-1,-1):
        temp=arr[i]
        arr[i]=next_greater

        if next_greater<temp:
            next_greater=temp
    return arr
# def print(arr):
#     for i in range(len(arr)):
#         print(arr[i])

arr=[17,18,5,4,6,1]
print(greater(arr))


