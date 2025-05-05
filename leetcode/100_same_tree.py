# do a breadth first search and make comparisons along the way
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    treelistone=[]
    treelisttwo=[]
    if p:
        treelistone.append(p)
    if q:
        treelisttwo.append(q)
    while treelistone or treelisttwo:
        if len(treelistone)!=len(treelisttwo):
            return False
        nexttreeone =[]
        nexttreetwo = []
        for i in range(0,len(treelistone)):
            p=treelistone[i]
            q=treelisttwo[i]
            # different values
            if p.val != q.val:
                return False
            # one side of one tree is missing, but not missing on both trees
            if (not p.left or not q.left) and (p.left or q.left):
                return False
            if (not p.right or not q.right) and (p.right or q.right):
                return False
            if p.left:
                nexttreeone.append(p.left)
                nexttreetwo.append(q.left)
            if p.right:
                nexttreeone.append(p.right)
                nexttreetwo.append(q.right)
        treelistone=nexttreeone
        treelisttwo=nexttreetwo
    return True