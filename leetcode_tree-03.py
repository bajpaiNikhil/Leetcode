

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def addi(root):
    sum=[0]
    traversal(root,sum)
def traversal(root:TreeNode,sum):
    if root:
        traversal(root.right,sum)
        sum[0]+=root.val
        root.val=sum[0]
        #print(sum)
        print(root.val)
        traversal(root.left,sum)
        return root

root=TreeNode(5)
root.left=TreeNode(2)
root.right=TreeNode(13)
addi(root)