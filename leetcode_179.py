





class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
l=[]
def print1(root):

    if root:
        l.append(root.val)
        print1(root.next)
    # return l
    f = list(map(str, l))
    return (int("".join(f), 2))

root=Node(0)
# root.next=Node(0)
# root.next.next=Node(1)
#
# e=print1(root)
# f=list(map(str,e))
# print(int("".join(f),2))
print(print1(root))


