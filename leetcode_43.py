root=[2,2,2,5,2]
##binary tree

"""

def unival(root):

    left_value= root.val==None or root.left.val=root.val and unvial(root.left)
    
    right_value= root.val==None or root.right.val=root.val and unival(root.right)
    
    return bool(left_value and right_value)

"""