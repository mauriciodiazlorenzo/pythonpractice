# perform a depth first traversal, keeping track of the depth

def maxDepth(self, root: Optional[TreeNode]) -> int:
    depth = 0
    treelist = []
    if root:
        treelist.append(root)
    while len(treelist) > 0:
        depth += 1
        nextlist = []
        for node in treelist:
            if node.left:  # not None
                nextlist.append(node.left)
            if node.right:  # not None
                nextlist.append(node.right)
        treelist = nextlist
    return depth