
def inorder(root,end):
    if root==None:
         return end

    res=inorder(root.left,root)
    root.left=None
    root.right=inorder(root.right,end)
    return res


root=[5,3,6,2,4,None,8,1,None,None,None,7,9]
print(inorder(root,end=None))
