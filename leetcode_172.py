



class treeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def tree(root):
    res=[]
    if root==None:
        return []

    pathleaf(root,"",res)
    return res

def pathleaf(root,string,res):
    string+=str(root.val)

    if root.left:
        pathleaf(root.left,string+"->",res)
    if root.right:
        pathleaf(root.right,string+"->",res)

    if not root.left and not root.right:
        res.append(string)
    return res
root=treeNode(1)
root.left=treeNode(4)
root.right=treeNode(5)
root.left.right=treeNode(6)
root.left.left=treeNode(2)
root.right.right=treeNode(3)
print(tree(root))