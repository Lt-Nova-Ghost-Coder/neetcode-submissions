# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.root = root
        def inorder(node, array):
            if node:
                inorder(node.left, array)
                array.append(node.val)
                inorder(node.right, array)
        
        inorderArray = []
        inorder(self.root, inorderArray)
        
        for i in range(1, len(inorderArray)):
            if inorderArray[i] > inorderArray[i - 1]:
                continue
            else:
                return False
        return True
        