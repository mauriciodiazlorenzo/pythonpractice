def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None
    ind = 0
    while ind < len(lists):
        if not lists[ind]:
            lists.pop(ind)
            ind -= 1
        ind += 1
    if not lists:
        return None
    headnode = None
    curnode = None
    while lists:
        minnode = None
        minind = -1
        minval = 1E6
        for ind, n in enumerate(lists):
            if n.val < minval:
                minval = n.val
                minnode = n
                minind = ind
        if minnode.next:
            lists[minind] = minnode.next
        else:
            lists.pop(minind)
        if headnode:
            curnode.next = minnode
            curnode = minnode
        else:
            headnode = minnode
            curnode = headnode
    return headnode
