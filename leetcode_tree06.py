

class treeNode:
    def __init__(self,val):
        self.val=val
        self.left=self.right=None

def invert(root):
    if root==None:
        return root

    left_=invert(root.left)
    right_=invert(root.right)

    root.left=right_
    root.right=left_

    return root

root=treeNode(1)
root.left=treeNode(2)
root.right=treeNode(3)
print(invert(root.right))