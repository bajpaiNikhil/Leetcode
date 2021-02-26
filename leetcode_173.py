


class treeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


def tree(root1,root2):
    if root1==None:
        return False

    if ismatch(root1,root2):
        return True
    return tree(root1.left,root2) or tree(root1.right,root2)

def ismatch(s,t):
    if not s and not t:
        return True
    if not s or not t:
        return False

    if s.val==t.val:
        if ismatch(s.left,t.left) and ismatch(s.right,t.right):
            return True
        else:
            return False

root1=treeNode(3)
root1.left=treeNode(4)
root1.left.left=treeNode(1)
root1.left.right=treeNode(2)
root1.left.right.left=treeNode(0)
root1.right=treeNode(5)


root2=treeNode(4)
root2.left=treeNode(1)
root2.right=treeNode(2)

print(tree(root1,root2))

