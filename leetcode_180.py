


class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next



def deleteNode(root,number):
    pass


root=Node(4)
root.next=Node(5)
root.next.next=Node(3)
root.next.next.next=Node(1)
number=5

print(deleteNode(root,number))