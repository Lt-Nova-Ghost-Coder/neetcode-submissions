# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.root = root
        self.subRoot = subRoot
        def preorder(root):
            if not root:
                return '#'
            
            return (str(root.val) + preorder(root.left) + preorder(root.right))
    
        string = preorder(self.root)
        subString = preorder(self.subRoot)
        if subString in string:
            return True
        return False
        