class listnode:
    def __init__(self,x):
        self.val=x
        self.next=None

    def middle(self,head):
        first=listnode()
        first.next=head

        faster=first
        slower=head
        while( faster is not None):
            if faster.next is not None:
                faster=faster.next
            faster=faster.next
            slower=slower.next

        return slower
r1=listnode([1,2,3,4,5])
print(r1.middle() )
