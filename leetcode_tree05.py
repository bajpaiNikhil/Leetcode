


class treeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def inorder(root,l):

    if root:
        inorder(root.left,l)
        #print(root.val)
        l.append(root.val)
        inorder(root.right,l)
        return (l)

root=treeNode(1)
root.left=treeNode(2)
#root.right=None
l=[]
print(inorder(root,l))
node=treeNode(1)
node.left=treeNode(None)
node.right=treeNode(2)
d=[]
print(inorder(node,d))
print(inorder(root,l)==inorder(node,d))

