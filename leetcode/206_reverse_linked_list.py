# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    prevnode = None
    curnode = head
    while curnode:
        nextnode = curnode.next
        curnode.next = prevnode
        prevnode = curnode
        curnode = nextnode
    return prevnode

