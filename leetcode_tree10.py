



class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def balancedHeight(root):

    if root==None:
        return True

    l=height(root.left)
    r=height(root.right)

    if abs(l-r)<=1 and balancedHeight(root.left) and balancedHeight(root.right):
        return True
    return False

def height(root):
    if root==None:
        return 0
    return 1+max(height(root.left),height(root.right))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(6)
root.left.left.right=TreeNode(7)
print(balancedHeight(root))