



class LinkNode:
    def __init__(self,val=0,link=None):
        self.val=val
        self.link=link

def oddEven(node):
    list1=[]

    current=node
    while current:
        list1.append(current.val)
        current=current.link

    odd=[]
    even=[]
    for i in range(len(list1)):
        if i%2!=0:
            odd.append(list1[i])
        else:
            even.append(list1[i])
    list2 =  even + odd

    head=LinkNode(list2[0])
    current=head
    for i in list2[1:]:
        current.link=LinkNode(i)
        current=current.link

    return head
node=LinkNode(2)
node.link=LinkNode(1)
node.link.link=LinkNode(3)
node.link.link.link=LinkNode(5)
node.link.link.link.link=LinkNode(6)
node.link.link.link.link.link=LinkNode(4)
node.link.link.link.link.link.link=LinkNode(7)

print(oddEven(node))

