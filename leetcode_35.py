#SEARCH IN A BST

"""

def searchbst(root,val)

    if root==None:
    return None
    if root.val==val:
    return root

    if val<root.val:
    return self.searchbst(root.left,val)
    else:
    return self.searchbst(root.right,val)


"""