"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# use map to store the copy and use the original as the key

def getOrCreateClone(node: 'Node') -> 'Node':
    if node in map:
        return map[node] # we already have a copy
    copy = Node(node.val,[])
    map[node]=copy
    for neighbour in node.neighbors:
        copy.neighbors.append(getOrCreateClone(neighbour))
    return copy

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        global map
        map = {}
        if not node:
            return node
        return getOrCreateClone(node)