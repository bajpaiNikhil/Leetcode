


class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next


def intersection(root1,root2):
    if root1 and root2:
        a,b=root1,root2

        while a!=b:
            a=a.next if a else b
            b=b.next if b else a
        return a

root1=Node(1)
root1.next=Node(9)
root1.next.next=Node(1)
root1.next.next.next=Node(2)
root1.next.next.next.next=Node(4)

root2=Node(3)
root2.next=Node(2)
root2.next.next=Node(4)


print(intersection(root1,root2))