


class NewNode:
    def __init__(self,val):
        self.val=val
        self.child=[]


def pre(root):
    n=[]
    if root==None:
        return None

    return travrese(root,n)

def travrese(root,n):

    n.append(root.val)

    for i in range(len(root.child)):
        n.extend(travrese(root.child[i],n))
    return n

root = NewNode(1)
root.child.append(NewNode(2))
root.child.append(NewNode(3))
root.child.append(NewNode(4))
root.child[0].child.append(NewNode(5))
root.child[0].child[0].child.append(NewNode(10))
root.child[0].child.append(NewNode(6))
root.child[0].child[1].child.append(NewNode(11))
root.child[0].child[1].child.append(NewNode(12))
root.child[0].child[1].child.append(NewNode(13))
root.child[2].child.append(NewNode(7))
root.child[2].child.append(NewNode(8))
root.child[2].child.append(NewNode(9))

print(pre(root))