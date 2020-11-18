
#
# class Node:
#     def __init__(self,data,left=None,right=None):
#         self.data=data
#         self.left=left
#         self.right=right
#
# def insert(root,key):
#
#     if root is None:
#         return Node(key)
#
#     if key<root.data:
#         root.left=insert(root.left,key)
#
#     else:
#         root.right=insert(root.right,key)
#
#     return root
#
#
# def findPair(root,sum,set):
#
#     if root==None:
#         return False
#     elif findPair(root.left,sum,set):
#         return True
#     elif (sum-root.data) in set:
#         print("Pair found at:",sum-root.data,root.data )
#         return True
#     else:
#         set.add(root.data)
#     findPair(root.right,sum,set)
#
#
# keys = [15, 10, 20, 8, 12, 16, 25]
# sum=28
# set=set()
#
# root=None
# for key in keys:
#     root=insert(root,key)
#
# if not findPair(root,sum,set):
#     print("404no pair found")


class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def insert(root,key):
    if root is None:
        return Node(key)
    root.left=insert(root.left,key)
    root.right=insert(root.right,key)
    return root

def traverse(root,list):
    if root:
        list.apppend(root.data)
        traverse(root.left,list)
        traverse(root.right,list)

def findTraget(root,traget):

    orilist=[]
    clolist=[]

    traverse(root,orilist)
    traverse(root,clolist)

    for n,m in zip(orilist,clolist):
        if n==traget:
            return m
if __name__ == '__main__':

    array=[7,4,3,None,None,6,19]
    traget=3
    root=None

    for i in array:
        root=insert(root,i)
    print(findTraget(root,traget))