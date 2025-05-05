# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# uses a lot of space, but probably no better solution
def hasCycle(self, head: Optional[ListNode]) -> bool:
    curnode = head
    map = {}
    while curnode:  # empty reference "None" casts to false
        if curnode in map:
            return True
        map[curnode] = True
        curnode = curnode.next
        # the list has an end, so return false
    return False
