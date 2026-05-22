# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.root = root
        self.k = k
        def inorder(node, array):
            if node:
                inorder(node.left, array)
                array.append(node.val)
                inorder(node.right, array)
        
        array = []
        inorder(self.root, array)
        return array[self.k - 1]