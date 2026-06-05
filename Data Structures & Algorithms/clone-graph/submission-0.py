"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.node = node
        if not self.node:
            return None
        Map = {}
        def dfs(node):
            if node in Map:
                return Map[node]
            cpy = Node(node.val)
            Map[node] = cpy

            for u in node.neighbors:
                cpy.neighbors.append(dfs(u))
            return cpy
        
        return dfs(self.node)

        