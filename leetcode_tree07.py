


class treeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def height(root):
    if root==None:
        return 0

    return 1+max(height(root.left),height(root.right))

root=treeNode(3)
root.left=treeNode(9)
root.right=treeNode(20)
root.left.left=treeNode(None)
root.left.right=treeNode(None)
root.right.right=treeNode(15)
root.right.left=treeNode(7)

print(height(root))

