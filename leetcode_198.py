



class listNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

# def isPalindrome(head):
#     if head:
#         l.append(head.val)
#         isPalindrome(head.next)
#     return l == l[::-1]

def isPalindrome(head):
    if not head or not head.next:
        return True

    fast  = slow = cur = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    stack=[slow.val]

    while slow.next:
        slow = slow.next
        stack.append(slow.val)
    while stack:
        if stack.pop() != cur.val:
            return False
        cur = cur.next
    return True




node=listNode(1)
node.next=listNode(2)
node.next.next=listNode(2)
node.next.next.next=listNode(1)
l=[]
print(isPalindrome(node))
