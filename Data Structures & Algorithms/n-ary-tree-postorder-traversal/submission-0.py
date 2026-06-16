"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.root = root
        def dfs(node, array):
            if node:
                for child in node.children:
                    dfs(child, array)
                array.append(node.val)
        
        ans = []
        dfs(self.root, ans)
        return ans
        