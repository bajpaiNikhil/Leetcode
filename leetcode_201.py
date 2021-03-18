# from queue import Queue
#
# #Q = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# def reverseTheReverse(Queue,k):
#
#     stack=[]
#
#     if Queue.empty() == True or k > Queue.qsize():
#         return
#     if k<=0:
#         return
#
#     for i in range(k):
#         stack.append(Queue.queue[0])
#         Queue.get()
#     while len(stack)!=0:
#         Queue.put(stack[-1])
#         stack.pop()
#
#     for i in range(Queue.qsize() - k):
#         Queue.put(Queue.queue[0])
#         Queue.get()
#
# def printQ(Queue):
#     while (not Queue.empty()):
#         print(Queue.queue[0], end =" ")
#         Queue.get()
#
# k = 5
#
# Queue=Queue()
# Queue.put(10)
# Queue.put(20)
# Queue.put(30)
# Queue.put(40)
# Queue.put(50)
# Queue.put(60)
# Queue.put(70)
# Queue.put(80)
# Queue.put(90)
# Queue.put(90)
# Queue.put(100)
# reverseTheReverse(Queue,k)
# #print(printQ(Queue))
# printQ(Queue)
#
#
#



def sub_lists(l,k):
    base = []
    lists = [base]
    for i in range(len(l)):
        orig = lists[:]
        new = l[i]
        for j in range(len(lists)):
            lists[j] = lists[j] + [new]
        lists = orig + lists

    li=lists[1:]
    suum = []
    for i in li:
        suum.append(sum(i) % k)
    a=max(suum)
    b=suum.count(max(suum))
    return a,b
n,k=map(int,input().split())
l =list(map(int,input().split()))
print(sub_lists(l,k))



#
# li=sub_lists(l)[1:]
#
# print(li[1:])
# suum=[]
# for i in li:
#     suum.append(sum(i)%k)
#
# print(suum)
# print(max(suum),suum.count(max(suum)))

