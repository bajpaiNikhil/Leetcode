"""Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5"""
def arraytoBST(nums):
    if nums==None:
        return None

    mid=len(nums)//2

    root=treenode(nums[mid])

    root.left=arraytoBST(nums[:mid])
    root.right=arraytoBST(nums[mid+1:])

    return root
