



class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def depth(root,n,level):
    if root==None:
        return 0
    if root.val==n:
        return level
    l=depth(root.left,n,level+1)
    if l!=0:
        return l
    l=depth(root.right,n,level+1)

    return l

def parent_search(root, child_node):
    if not root: return None
    if root.left and root.left.val==child_node: return root.val
    if root.right and root.right.val==child_node: return root.val
    return parent_search(root.left, child_node) or parent_search(root.right, child_node)

def cusion(root,n,m):
    if (depth(root,n,0)== depth (root,m,0)):
        if parent_search(root,n)!=parent_search(root,m):
            return True
        else:
            return False
    return False



root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(None)
root.left.right=TreeNode(4)
root.right.right=TreeNode(5)
n=4
# print(parent_search(root,n))
m=5
# print(parent_search(root,m))
# print(parent_search(root,n)==parent_search(root,m))

# print(depth(root,n,0) == depth(root,m,0) )
print(cusion(root,n,m))
