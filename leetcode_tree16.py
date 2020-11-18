





class treeNode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def height(root):
    if root is None:
        return 0
    else:
        return max(height(root.left),height(root.right))+1

def heightsum(root,k,sum):
    if root is None:
        return
    if k==0:
        #print(root.val)
        if root.val!=None:
            #sum+=root.val
            #print(root.val)
            sum.append(root.val)
    else:
        heightsum(root.left,k-1,sum)
        heightsum(root.right,k-1,sum)
    return sum

if __name__ == '__main__':
    sum=[]

    root = treeNode(3)
    root.left = treeNode(9)
    root.right = treeNode(20)
    root.left.left = treeNode(None)
    root.left.right = treeNode(None)
    root.right.right = treeNode(15)
    root.right.left = treeNode(7)

    print(height(root))
    print(heightsum(root,2,sum))
    d=heightsum(root,2,sum)
    o=0
    for i in set(d):
        o+=i
    print(o)

