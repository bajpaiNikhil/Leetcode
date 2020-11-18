


class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def same(root,node):
    if root==None:
        return False
    elif subset(root,node):
        return True
    else:
        return subset(root.left,node) or subset(root.right,node)


def subset(root,node):
    if root==None or node==None:
        return root==None and node==None
    elif root.val==node.val:
        return subset(root.left,node.left) and subset(root.right,node.right)
    else:
        return False


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(6)
root.left.left.right=TreeNode(7)

node=TreeNode(4)
node.left=TreeNode(6)
node.right=TreeNode(7)

print(same(root,node))