






from queue import Queue

#Q = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
def reverseTheReverse(Queue,k):
    stack=[]
    if Queue.empty() == True or k > Queue.qsize():
        return
    if k<=0:
        return

    for i in range(k):
        stack.append(Queue.queue[0])
        Queue.get()
    while len(stack)!=0:
        Queue.put(stack[-1])
        stack.pop()

    for i in range(Queue.qsize() - k):
        Queue.put(Queue.queue[0])
        Queue.get()

def printQ(Queue):
    while (not Queue.empty()):
        print(Queue.queue[0], end =" ")
        Queue.get()

k = 5
Queue=Queue()
Queue.put(10)
Queue.put(20)
Queue.put(30)
Queue.put(40)
Queue.put(50)
Queue.put(60)
Queue.put(70)
Queue.put(80)
Queue.put(90)
Queue.put(90)
Queue.put(100)
print(reverseTheReverse(Queue,k))
print(printQ(Queue))