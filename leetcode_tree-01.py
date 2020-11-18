

#Tile of a tree
class Treenode:
    def __init__(self,val):

        self.left=None
        self.right=None
        self.val=val


def binarytilt(root:Treenode,tile):
    if root==None:
        return 0

    left=binarytilt(root.left,tile)
    right=binarytilt(root.right,tile)
    tile[0]+=abs(left-right)
    return left+right+root.val

def Tile(root):
    tile=[0]
    binarytilt(root,tile)
    return tile[0]

root=Treenode(1)
root.left=Treenode(4)
root.right=Treenode(5)
root.left.left=Treenode(2)
root.right.right=Treenode(3)
# root.left=Treenode(1)
# root.right=Treenode(3)
print(Tile(root))
