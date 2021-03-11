

class treeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
l=[]
def inorder(root):
    if root==None:
        return None

    inorder(root.left)
    #print(root.val)
    l.append(root.val)
    inorder(root.right)
    return l
root=treeNode(5)
root.left=treeNode(1)
root.right=treeNode(4)
root.right.right=treeNode(6)
root.right.left=treeNode(3)

print(inorder(root))
e=inorder(root)

if e==sorted(e):
    print(True)
else:
    print(False)