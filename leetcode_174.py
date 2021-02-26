



class treeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def pruning(root):
    if root==None:
        return False
    if not containsOne(root):
        root = None
    return root

def containsOne(root):

    if root==None:
        return False

    left_constains=containsOne(root.left)
    right_constains=containsOne(root.right)

    if not left_constains:
        root.left=None
    if not right_constains:
        root.right=None
    return root.val==1 or left_constains or right_constains

root=treeNode(1)
root.left=treeNode(1)
root.right=treeNode(0)
root.left.left=treeNode(1)
root.left.right=treeNode(0)
root.right.left=treeNode(0)

print(pruning(root))