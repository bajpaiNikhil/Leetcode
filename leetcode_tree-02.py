
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def uniValued(root:TreeNode):
    left_= root.left == None or root.left.val == root.val and uniValued(root.left)
    right_= root.right == None or root.right.val == root.val and uniValued(root.right)
    print(left_,right_)
    return bool(left_ and right_)

root=TreeNode(None)
root.left=TreeNode(1)
root.right=TreeNode(1)
root.left.left=TreeNode(2)
print(uniValued(root))