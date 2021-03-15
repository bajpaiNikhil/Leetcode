


class listNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def merge(node,node1):
    list1=[]
    current=node
    while current:
        list1.append(current.val)
        current=current.next
    print(list1)

    list2=[]
    current = node1

    while current:
        list2.append(current.val)
        current=current.next
    print(list2)

    list3=list1[:a]+list2+list1[b+1:]
    if len(list3)==0:
        return None
    print(list3)

    head=listNode(list3[0])
    current=head
    for i in list3[1:]:
        current.next=listNode(i)
        current = current.next
    return (head)
node=listNode(0)
node.next=listNode(1)
node.next.next=listNode(2)
node.next.next.next=listNode(3)
node.next.next.next.next=listNode(4)
node.next.next.next.next.next=listNode(5)

a,b=3,4

node1=listNode(1000000)
node1.next=listNode(1000001)
node1.next.next=listNode(1000002)

print(merge(node,node1))
