# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.root = root
        self.p = p
        self.q = q

        while self.root:
            if (self.p.val < self.root.val and self.q.val < self.root.val):
                self.root = self.root.left
            elif (self.p.val > self.root.val and self.q.val > self.root.val):
                self.root = self.root.right
            else:
                return self.root
        
        

        

        