

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def sym(root):
    if root==None:
        return True
    return mirror(root.left,root.right)

def mirror(left_ , right_):
    if left_== None or right_== None:
        return (left_==right_)
    if left_.val!=right_.val:
        return False
    return mirror(left_.left,right_.right) and mirror(left_.right , right_.left)

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(2)
root.left.left=None
root.left.right=TreeNode(4)
root.right.right=None
root.right.left=TreeNode(4)

print(sym(root))



